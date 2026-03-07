# 🔐 Secure Vault: Flask-Based Password Manager

A lightweight, local-first web application designed to store, generate, and manage digital credentials securely. Built with **Python** and **Flask**, this project demonstrates a complete **CRUD** (Create, Read, Update, Delete) lifecycle with a focus on **Conditional Data Retrieval** for enhanced privacy.



---

## 🚀 Key Features

* **Session-Based Authentication:** A secure login gate prevents unauthorized users from accessing the vault data.
* **Privacy-First Retrieval:** Unlike standard managers, the vault remains "hidden" by default. Data is only rendered when a specific search query is executed, preventing "shoulder-surfing" exposure.
* **Smart Password Logic:** Features an automated generator that creates high-entropy, randomized passwords if the user leaves the input blank.
* **Persistent Storage:** Uses a structured `JSON` backend, making the database portable and easy to back up without complex SQL setups.
* **Clean UI/UX:** A responsive, CSS3-styled interface with a focus on simplicity and ease of use.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.13 / Flask
* **Templating:** Jinja2 (Dynamic HTML rendering)
* **Frontend:** HTML5 / CSS3
* **Storage:** JSON (Flat-file database)

---

## 📦 Project Structure

```text
Josh_23/
├── app.py             # Main Flask application logic
├── data.json          # Local storage (Excluded from Git via .gitignore)
├── templates/         # UI Components
│   ├── index.html     # Main Vault Dashboard
│   └── login.html     # Security Gateway
└── README.md          # Project Documentation
\```



---

## ⚙️ Setup & Installation

### 1. Clone the Repository
\```bash
git clone [https://github.com/YOUR_USERNAME/SecureVault.git](https://github.com/YOUR_USERNAME/SecureVault.git)
cd SecureVault
\```

### 2. Install Dependencies
\```bash
pip install flask
\```

### 3. Run the Application
\```bash
python app.py
\```

### 4. Access the Vault
Open your browser and navigate to: `http://127.0.0.1:8080`
* **Username:** `josh`
* **Password:** `1234`

---

## ✅ Development Roadmap
- [x] User Authentication & Sessions
- [x] Search-to-Reveal Logic
- [x] Automatic Password Generator
- [ ] Implement Bcrypt Hashing for Master Password
- [ ] Add "Copy to Clipboard" buttons for passwords

---

## 🛡️ Security Note
This project is intended for educational purposes. For production use, it is recommended to implement password hashing (e.g., `Bcrypt`) and utilize environment variables for the `SECRET_KEY`.

---
