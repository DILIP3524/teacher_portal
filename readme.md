# 📝 Teacher Portal Web Application (Django)

A **secure teacher portal** built with **Django** that allows authenticated teachers to manage students, their subjects, and marks with proper validation and security controls.  

This project is based on the task **“Building a Secure, Logic-Driven Teacher Portal”** and demonstrates custom authentication, session handling, and backend logic without relying on Django’s built-in auth system.  

---

## 🚀 Features
- **Custom Authentication**  
  - Passwords hashed + salted (manual implementation, no Django auth).  
  - Session handling with custom in-memory session tokens stored in cookies.  

- **Teacher Dashboard**  
  - List of students with: Name, Subject, Marks.  
  - Inline edit button .  
  - Inline deletion of student records.  
  - Audit logging of all mark updates with timestamp and teacher info.  

- **Add Student Modal**  
  - form to add new students.  
  - If a student with the same name & subject exists → update marks using a helper (`calculate_new_marks`).  
  - Otherwise, create a new record.  
  - Prevent total marks from exceeding 100.  

- **Security Measures**  
  - Input validation (client + server side).  
  - Parameterized queries via Django ORM (prevents SQL Injection).  
  - Passwords stored securely with hashing + salting.  
  - Protection against **XSS** (escaped templates) and **CSRF** (form tokens).  

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/DILIP3524/teacher-portal.git
cd teacher-portal
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Activate
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start Development Server
```bash
python manage.py runserver
```

Visit 👉 http://127.0.0.1:8000/  

---

## 📌 Security Considerations
- Manual authentication (no Django auth).  
- Passwords hashed + salted before saving.  
- Sessions handled in-memory with secure cookies.  
- All inputs validated both client-side and server-side.  
- CSRF tokens used in forms.

---

## 📊 Evaluation Alignment
- ✅ Custom login + session handling (manual)  
- ✅ Secure password storage and input validation  
- ✅ Audit logging for marks update  
- ✅ Inline editing & deletion of student records  
- ✅ Modal-based student addition with duplicate check  
- ✅ No reliance on AI or built-in Django authentication  

---

## ⏱️ Development Notes
- **Challenges faced**:  

  - Implementing custom password hashing and secure session handling.  
 

- **Approximate time taken**: ~8-9 hours  

---

## 🛠️ Tech Stack
- **Backend**: Django 5, Python 3  
- **Database**: SQLite
- **Frontend**: Bootstrap 5
- **Version Control**: Git  

---

## 📂 Project Structure

```
teacher-portal/
│
├── portal/               # Main app (students, teachers, auth, utils)
│   ├── models.py         # Teacher, Student, AuditLog
│   ├── views.py          # Auth & student management views
│   ├── utils.py          # Custom hashing & session logic
│   ├── forms.py          # Login, Register, Student forms
│   └── templates/        # HTML templates
│
├── teacher_portal/       # Django project settings
│
├── db.sqlite3            # SQLite database
├── requirements.txt      # Dependencies
├── manage.py             # Django CLI
└── README.md             # Documentation
```

---

## 👤 Author
**Dilip Kumar**  
📧 Email: dilip3524@gmail.com  
🐱 GitHub: [@DILIP3524](https://github.com/DILIP3524)  
