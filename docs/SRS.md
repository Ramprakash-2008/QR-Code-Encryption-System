# 🔐 Software Requirements Specification (SRS)

> **Project:** QR Code Encryption System  
> **Version:** 1.0.0  
> **Author:** Ramprakash  
> **Framework:** Flask (Python)

---

# 📖 Introduction

The **QR Code Encryption System** is a secure web application developed using **Python**, **Flask**, and **SQLite**. The system enables controlled access to shared files through QR codes by combining **UUID-based token generation**, **email approval**, and **database-driven authorization**.

Unlike traditional QR codes that expose a direct file link, this application generates a secure access token, ensuring that only approved users can access the shared resource.

---

# 🎯 Project Objective

Develop a secure QR-based file-sharing system that:

- ✅ Generates unique QR codes
- ✅ Prevents unauthorized access
- ✅ Uses email approval before granting access
- ✅ Maintains request records
- ✅ Demonstrates secure software engineering concepts

---

# ❗ Problem Statement

Traditional QR codes directly expose URLs.

Anyone with the QR code can access the linked content.

There is **no identity verification** or **owner approval** before access.

---

# 💡 Proposed Solution

This system introduces a secure approval workflow.

```text
Generate QR
      │
      ▼
Store UUID Token
      │
      ▼
User Scans QR
      │
      ▼
User Enters Gmail
      │
      ▼
Owner Receives Email
      │
      ▼
Approve / Reject
      │
      ▼
Access Granted
```

---

# ✨ Functional Requirements

| ID | Requirement |
|----|-------------|
| FR-01 | Generate secure QR codes |
| FR-02 | Generate UUID tokens |
| FR-03 | Store request details |
| FR-04 | Collect user Gmail |
| FR-05 | Email owner for approval |
| FR-06 | Approve or deny requests |
| FR-07 | Redirect approved users |
| FR-08 | Maintain request status |

---

# ⚙️ Non-Functional Requirements

- Fast response time
- Lightweight application
- Easy deployment
- Secure token generation
- Simple UI
- Maintainable code

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| SQLite | Database |
| SMTP | Email Service |
| UUID | Token Generation |
| QRCode | QR Creation |
| HTML/CSS | Frontend |

---

# ⚠️ Current Limitations

- SQLite is intended for lightweight deployments.
- No login system.
- Tokens do not expire.
- Password protection is not available yet.

---

# 🚀 Future Enhancements

- AES Encryption
- Password-Protected QR
- Login System
- Expiring QR Tokens
- Admin Dashboard
- Access Logs
- Cloud Storage

---

> 💡 **Note**
>
> This project is designed to demonstrate secure file sharing concepts and software architecture using QR technology.
