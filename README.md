# 🔐 QR Code Encryption System

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask" />
<img src="https://img.shields.io/badge/QR_Code-Generator-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Cryptography-Secure-red?style=for-the-badge" />
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />

</p>

<p align="center">
<b>A Secure QR Code Based Encryption & Decryption Web Application</b>

Encrypt sensitive information, generate secure QR Codes, and decrypt them safely using Python and Flask.
</p>

---

# 📖 Table of Contents

- About the Project
- Key Features
- Problem Statement
- Solution
- Technology Stack
- System Workflow
- Project Architecture
- Project Structure
- Installation
- Usage
- Screenshots
- Security Features
- Future Scope
- Learning Outcomes
- Contributing
- Author
- License

---

# 📌 About the Project

The **QR Code Encryption System** is a web application developed using **Python** and **Flask** that securely encrypts confidential information and converts it into a QR Code for safe storage and sharing.

Instead of transmitting plain text directly, the application encrypts the information first and then embeds the encrypted content inside a QR Code.

The receiver scans the QR Code and decrypts the encrypted information to retrieve the original message.

This project demonstrates the practical implementation of **Cryptography** together with **QR Code Technology** for secure communication.

---

# ❗ Problem Statement

Sensitive information is often shared as plain text through messaging platforms, emails, or documents.

This approach introduces several security risks including:

- Unauthorized access
- Data interception
- Information leakage
- Easy readability by attackers

A secure mechanism is required to protect sensitive information before sharing.

---

# ✅ Proposed Solution

The QR Code Encryption System solves this problem by:

1. Accepting user input.
2. Encrypting the entered information.
3. Generating a QR Code containing the encrypted data.
4. Allowing secure sharing of the QR Code.
5. Decrypting the scanned QR Code back to its original message.

---

# ✨ Features

- 🔒 Secure Data Encryption
- 📷 QR Code Generation
- 🔓 QR Code Decryption
- 💾 Download Generated QR Code
- 🌐 User-Friendly Web Interface
- ⚡ Fast Encryption & Decryption
- 📱 QR Code Sharing Support
- 🛡 Secure Communication Workflow

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Flask | Web Framework |
| HTML5 | User Interface |
| CSS3 | Styling |
| JavaScript | Frontend Interaction |
| QRCode Library | QR Code Generation |
| Cryptography Library | Data Encryption |

---

# 🔄 System Workflow

```text
                User

                  │

                  ▼

          Enter Sensitive Data

                  │

                  ▼

        Encryption Algorithm

                  │

                  ▼

          Encrypted Message

                  │

                  ▼

         QR Code Generation

                  │

                  ▼

       Download / Share QR

                  │

                  ▼

        Scan QR Code Later

                  │

                  ▼

         Extract Cipher Text

                  │

                  ▼

        Decryption Algorithm

                  │

                  ▼

         Original Information
```

---

# 🏗 Project Architecture

```text
                Browser

                    │

                    ▼

             Flask Application

          ┌─────────┴──────────┐

          │                    │

          ▼                    ▼

 Encryption Module      QR Generator

          │                    │

          └─────────┬──────────┘

                    ▼

             Generated QR Code

                    │

                    ▼

              Download / Share
```

---

# 📂 Project Structure

```text
QR-Code-Encryption-System/

│

├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│
├── screenshots/
│
├── docs/
│   ├── SRS.md
│   ├── ARCHITECTURE.md
│   ├── FLOW.md
│   └── CHANGELOG.md
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── .env
```

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/Ramprakash-2008/QR-Code-Encryption-System.git
```

---

## Navigate to Project Directory

```bash
cd QR-Code-Encryption-System
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

---

## Open in Browser

```
http://127.0.0.1:5000
```

---

# 💻 Usage

### Encrypt

- Enter the confidential message.
- Click **Encrypt**.
- Generate the QR Code.
- Download or share the generated QR Code.

### Decrypt

- Scan the generated QR Code.
- Extract the encrypted content.
- Click **Decrypt**.
- View the original message.

---

# 📸 Screenshots

> Screenshots will be added soon.

```
📷 Home Page

📷 Encryption Page

📷 QR Generation

📷 Decryption Page

📷 Output
```

---

# 🔒 Security Features

- Encrypts sensitive information before QR generation.
- QR Code stores encrypted data instead of plain text.
- Reduces the risk of exposing confidential information.
- Demonstrates secure communication using cryptography.
- Easy to share without exposing original content.

---

# 📈 Advantages

- Secure communication
- Fast QR generation
- Simple user interface
- Lightweight application
- Easy deployment
- Cross-platform compatibility

---

# 🚀 Future Scope

Future enhancements planned for this project include:

- AES-256 Encryption
- Password-Protected QR Codes
- User Authentication
- File Encryption Support
- Cloud Storage
- Email Integration
- QR Expiration
- Encryption History
- Secure File Sharing
- Multi-Algorithm Encryption

---

# 📚 Learning Outcomes

This project helped in understanding:

- Flask Web Development
- Python Backend Programming
- QR Code Generation
- Cryptography Concepts
- Secure Data Transmission
- Web Application Development
- Software Design Principles

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

# 👨‍💻 Author

## Ramprakash

Computer Science Engineering Student

### Connect with me

- GitHub: https://github.com/Ramprakash-2008

---

# ⭐ Show Your Support

If you found this project useful,

please consider giving it a ⭐ on GitHub.

It motivates me to build more open-source projects.

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project for educational purposes.

---

<p align="center">

<b>🔐 Secure Communication Starts with Encryption 🔐</b>

Made with ❤️ by <b>Ramprakash</b>

</p>
