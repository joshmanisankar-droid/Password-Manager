# 🔐 Secure Vault: Flask Password Manager

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-3.1.0-green.svg)](https://flask.palletsprojects.com/)

A lightweight, local-first web application designed to store and manage digital credentials securely. Built with **Python** and **Flask**, this project focuses on **Conditional Data Retrieval**—passwords stay hidden until you specifically search for them.



---

## 🚀 Key Features

* **🔒 Session Authentication:** Secure login gateway to protect your data.
* **🕵️ Privacy-First Search:** Data is only rendered when searched, preventing "shoulder-surfing" exposure.
* **🎲 Auto-Generator:** Generates high-entropy passwords automatically if the input is left blank.
* **📂 JSON Persistence:** Lightweight, portable database for easy backups.
* **📱 Responsive UI:** Clean, modern design built with CSS3 and Jinja2 templates.

---

## 📦 Project Structure

```text
Josh_23/
├── app.py             # Backend server & routing logic
├── data.json          # Private storage (Excluded via .gitignore)
├── .gitignore         # Security: Prevents sensitive file uploads
├── requirements.txt   # Configuration: Project dependencies
└── templates/         # UI Components
    ├── index.html     # Main Dashboard & Search
    └── login.html     # Security Gateway
\```

---

## 🛠️ Setup & Installation

### 1. Clone the Repository
\```bash
git clone [https://github.com/joshmanisankar-droid/Password-Manager.git](https://github.com/joshmanisankar-droid/Password-Manager.git)
cd Password-Manager
\```

### 2. Install Dependencies
\```bash
pip install -r requirements.txt
\```

### 3. Run the Application
\```bash
python app.py
\```

> **Note:** Access the vault at `http://127.0.0.1:8080`.  
> **Default Login:** `josh` / `1234`

---

## ✅ Development Roadmap
- [x] User Authentication & Sessions
- [x] Search-to-Reveal Logic
- [x] Automatic Password Generator
- [ ] Implement Bcrypt Hashing for Master Password
- [ ] Add "Copy to Clipboard" buttons

---

## 🛡️ Security Disclaimer
This project is intended for **educational purposes**. For production use, please implement password hashing and environment variables for the `SECRET_KEY`.
