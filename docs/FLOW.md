# 🔄 Project Workflow

> Complete execution flow of the QR Code Encryption System.

---

# 🚀 QR Generation Workflow

```text
Owner
  │
  ▼
Enter File Link
  │
  ▼
Generate UUID
  │
  ▼
Store in Database
  │
  ▼
Generate QR Code
  │
  ▼
Download QR
```

---

# 📲 User Access Workflow

```text
User
  │
  ▼
Scan QR
  │
  ▼
Open Web Page
  │
  ▼
Enter Gmail
  │
  ▼
Database Update
  │
  ▼
Email Sent to Owner
```

---

# 📧 Approval Workflow

```text
Owner
  │
  ▼
Receive Email
  │
  ▼
Approve / Reject
  │
  ▼
Update Database
  │
  ▼
Notify User
```

---

# ✅ Successful Access

```text
Scan QR Again
      │
      ▼
Enter Approved Gmail
      │
      ▼
Verification
      │
      ▼
Redirect to File
```

---

# ❌ Rejected Request

```text
User Request

↓

Owner Rejects

↓

Status Updated

↓

Denial Email Sent

↓

Access Blocked
```

---

# 📊 Complete System Flow

```text
Generate QR
      │
      ▼
Store Token
      │
      ▼
User Scan
      │
      ▼
Collect Gmail
      │
      ▼
Owner Approval
      │
      ▼
Database Update
      │
      ▼
Grant / Deny Access
```

---

> 💡 **Workflow Summary**
>
> The application ensures that possession of a QR code alone is not sufficient to access the protected file. Owner approval is required before access is granted.
