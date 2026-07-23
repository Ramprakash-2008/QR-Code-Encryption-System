import os
import uuid
import qrcode

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file
)

from werkzeug.utils import secure_filename

from config import Config

from database import (
    init_db,
    create_request,
    get_request_by_token,
    update_request_to_pending,
    approve_request,
    deny_request,
    get_all_requests
)

from email_service import send_email


# ========================================
# FLASK APPLICATION SETUP
# ========================================

app = Flask(__name__)

# Initialize database
init_db()


# ========================================
# FILE UPLOAD CONFIGURATION
# ========================================

UPLOAD_FOLDER = "uploads"

# Maximum file size: 50 MB
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024


# Create uploads directory
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ========================================
# HOME
# ========================================

@app.route("/")
def home():

    return redirect(
        url_for("generate_qr")
    )


# ========================================
# GENERATE QR CODE
# ========================================

@app.route(
    "/generate",
    methods=["GET", "POST"]
)
def generate_qr():

    if request.method == "POST":

        try:

            # Get file link
            file_link = request.form.get(
                "file_link"
            )

            # Get uploaded file
            uploaded_file = request.files.get(
                "file"
            )

            # Initially no file path
            file_path = None


            # ====================================
            # VALIDATE INPUT
            # ====================================

            if (
                not file_link
                and (
                    not uploaded_file
                    or uploaded_file.filename == ""
                )
            ):
                return (
                    "Please provide a file link "
                    "or upload a file.",
                    400
                )


            # ====================================
            # HANDLE FILE UPLOAD
            # ====================================

            if (
                uploaded_file
                and uploaded_file.filename
            ):

                # Secure filename
                original_filename = secure_filename(
                    uploaded_file.filename
                )

                # Generate unique filename
                unique_filename = (
                    f"{uuid.uuid4()}_"
                    f"{original_filename}"
                )

                # Full file path
                file_path = os.path.join(
                    UPLOAD_FOLDER,
                    unique_filename
                )

                # Save uploaded file
                uploaded_file.save(
                    file_path
                )


                # No external link needed
                file_link = None


            # ====================================
            # CREATE TOKEN
            # ====================================

            token = str(
                uuid.uuid4()
            )


            # ====================================
            # SAVE REQUEST
            # ====================================

            create_request(
                token=token,
                file_link=file_link,
                file_path=file_path
            )


            # ====================================
            # CREATE QR URL
            # ====================================

            qr_url = (
                f"{Config.BASE_URL}"
                f"/request/{token}"
            )


            # ====================================
            # CREATE QR DIRECTORY
            # ====================================

            qr_dir = os.path.join(
                "static",
                "qr"
            )

            os.makedirs(
                qr_dir,
                exist_ok=True
            )


            # ====================================
            # QR IMAGE PATH
            # ====================================

            img_path = os.path.join(
                qr_dir,
                f"{token}.png"
            )


            # ====================================
            # GENERATE QR
            # ====================================

            img = qrcode.make(
                qr_url
            )

            img.save(
                img_path
            )


            # ====================================
            # DOWNLOAD QR
            # ====================================

            return send_file(
                img_path,
                as_attachment=True
            )


        except Exception as e:

            print(
                "Error generating QR:",
                e
            )

            return (
                "Internal Server Error",
                500
            )


    return render_template(
        "generate.html"
    )


# ========================================
# QR REQUEST / GMAIL VERIFICATION
# ========================================

@app.route(
    "/request/<token>",
    methods=["GET", "POST"]
)
def handle_qr_or_request(token):

    # Get request
    row = get_request_by_token(
        token
    )


    # Invalid token
    if not row:

        return (
            "❌ Invalid or expired token.",
            404
        )


    # Get stored information
    (
        approved_gmail,
        file_link,
        file_path,
        status
    ) = row


    # ====================================
    # GMAIL SUBMISSION
    # ====================================

    if request.method == "POST":

        gmail = request.form.get(
            "gmail"
        )


        # Validate Gmail
        if not gmail:

            return (
                "❌ Gmail is required.",
                400
            )


        # =================================
        # ALREADY APPROVED
        # =================================

        if (
            status == "approved"
            and gmail == approved_gmail
        ):

            # External file link
            if file_link:

                return redirect(
                    file_link
                )


            # Uploaded file
            if file_path:

                return send_file(
                    file_path,
                    as_attachment=True
                )


        # =================================
        # NEW ACCESS REQUEST
        # =================================

        update_request_to_pending(
            token,
            gmail
        )


        # Approval URL
        approve_url = url_for(
            "process_request",
            action="approve",
            token=token,
            _external=True
        )


        # Denial URL
        deny_url = url_for(
            "process_request",
            action="deny",
            token=token,
            _external=True
        )


        # Email body
        email_body = f"""
        <h3>New File Access Request</h3>

        <p>
        User Gmail:
        <strong>{gmail}</strong>
        </p>

        <p>
        <a href="{approve_url}">
        Approve Request
        </a>
        </p>

        <p>
        <a href="{deny_url}">
        Deny Request
        </a>
        </p>
        """


        # Send approval email
        send_email(
            Config.OWNER_EMAIL,
            "File Access Request",
            email_body
        )


        return render_template(
            "success.html"
        )


    # ====================================
    # GET REQUEST
    # ====================================

    if status == "approved":

        return render_template(
            "request_form.html",
            token=token,
            info=(
                "✅ Token approved. "
                "Please enter Gmail to continue."
            )
        )


    return render_template(
        "request_form.html",
        token=token
    )


# ========================================
# APPROVE / DENY REQUEST
# ========================================

@app.route(
    "/process/<action>/<token>"
)
def process_request(
    action,
    token
):

    # Get request
    row = get_request_by_token(
        token
    )


    # Invalid token
    if not row:

        return (
            "❌ Invalid or expired token.",
            404
        )


    # Gmail
    gmail = row[0]


    # ====================================
    # APPROVE
    # ====================================

    if action == "approve":

        approve_request(
            token
        )


        send_email(
            gmail,
            "Access Approved",
            """
            <h3>✅ Access Approved</h3>

            <p>
            Your request has been approved.
            </p>

            <p>
            Scan the QR code again to
            access the file.
            </p>
            """
        )


    # ====================================
    # DENY
    # ====================================

    elif action == "deny":

        deny_request(
            token
        )


        send_email(
            gmail,
            "Access Denied",
            """
            <h3>❌ Access Denied</h3>

            <p>
            Your request was denied.
            </p>
            """
        )


    # ====================================
    # INVALID ACTION
    # ====================================

    else:

        return (
            "❌ Invalid action.",
            400
        )


    return (
        f"User has been "
        f"{action}d successfully."
    )


# ========================================
# DEBUG REQUESTS
# ========================================

@app.route(
    "/debug/requests"
)
def debug_requests():

    rows = get_all_requests()


    return {
        "requests": rows
    }


# ========================================
# RUN APPLICATION
# ========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )