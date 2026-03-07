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

To maintain a clean MVC-style (Model-View-Controller) architecture, the files are organized as follows:

```text
Josh_23/
├── app.py             # Backend: Flask server & routing logic
├── data.json          # Database: Local JSON storage (Private)
├── .gitignore         # Security: Prevents sensitive files from being uploaded
├── requirements.txt   # Configuration: Lists necessary Python libraries
└── templates/         # Frontend: HTML UI components
    ├── index.html     # Main Dashboard (Vault & Search)
    └── login.html     # Authentication Gateway
\```

