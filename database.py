import sqlite3
from config import Config


def get_connection():
    """Create and return a database connection."""
    return sqlite3.connect(Config.DB_PATH)


def init_db():
    """Create the requests table if it does not exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                token TEXT UNIQUE NOT NULL,
                gmail TEXT,
                file_link TEXT,
                file_path TEXT,
                status TEXT NOT NULL,
                approved_at DATETIME
            )
        """)


def create_request(token, file_link=None, file_path=None):
    """Create a new file access request."""

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO requests
            (token, file_link, file_path, status)
            VALUES (?, ?, ?, ?)
            """,
            (
                token,
                file_link,
                file_path,
                "new"
            )
        )


def get_request_by_token(token):
    """Get a request using its unique token."""

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT gmail, file_link, file_path, status
            FROM requests
            WHERE token = ?
            """,
            (token,)
        )

        return cursor.fetchone()


def update_request_to_pending(token, gmail):
    """Store Gmail and change request status to pending."""

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE requests
            SET gmail = ?,
                status = ?,
                approved_at = NULL
            WHERE token = ?
            """,
            (
                gmail,
                "pending",
                token
            )
        )


def approve_request(token):
    """Approve a request and store approval time."""

    from datetime import datetime

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE requests
            SET status = ?,
                approved_at = ?
            WHERE token = ?
            """,
            (
                "approved",
                datetime.now(),
                token
            )
        )


def deny_request(token):
    """Deny a request."""

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE requests
            SET status = ?
            WHERE token = ?
            """,
            (
                "denied",
                token
            )
        )


def get_all_requests():
    """Get all requests for debugging or administration."""

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                token,
                gmail,
                file_link,
                file_path,
                status
            FROM requests
            """
        )

        return cursor.fetchall()