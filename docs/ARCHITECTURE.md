# 🏗️ System Architecture

> High-Level Design of the QR Code Encryption System

---

# 📌 Overview

The application follows a simple layered architecture where the Flask application coordinates user requests, database operations, QR generation, and email notifications.

---

# 🏛 Architecture Diagram

```text
                   👤 User
                      │
                      ▼
             🌐 Flask Application
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
📷 QR Generator   📧 Email Service   🗄 SQLite
      │
      ▼
 QR Code Image
```

---

# 🧩 Components

## 🌐 Flask Application

Responsible for:

- Handling HTTP requests
- Processing forms
- Generating QR codes
- Managing approvals
- Redirecting users

---

## 📷 QR Generator

Creates QR codes containing secure URLs based on UUID tokens.

---

## 📧 Email Service

Uses Gmail SMTP to send:

- Approval requests
- Approval confirmation
- Access denial notifications

---

## 🗄 Database

Stores:

| Field | Description |
|--------|-------------|
| Token | Unique Identifier |
| Gmail | User Email |
| File Link | Protected Resource |
| Status | Pending / Approved / Denied |
| Approved At | Approval Timestamp |

---

# 🔄 Request Lifecycle

```text
Owner

↓

Generate QR

↓

Database Entry

↓

QR Download

↓

User Scan

↓

Email Request

↓

Owner Approval

↓

Access Granted
```

---

> 💡 **Design Goal**
>
> Separate the QR code from the actual file URL using UUID tokens to improve access control.
