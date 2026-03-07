import json 
from flask import Flask, render_template, request, redirect, url_for, session
import random
import string
app = Flask(__name__)
app.secret_key = "josh_vault_key_2026"
USER_DATA = {"josh": "1234"} 
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(12))
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in USER_DATA and USER_DATA[username] == password:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "<h2>Access Denied: Wrong Username or Password</h2><a href='/login'>Try Again</a>"
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    search_query = request.args.get('search', '').lower()
    all_passwords = load_data()
    display_passwords = {}

    if search_query:
        display_passwords = {k: v for k, v in all_passwords.items() if search_query in k.lower()}
    return render_template('index.html', passwords=display_passwords, search_query=search_query)
@app.route('/add', methods=['POST'])
def add():
    if not session.get('logged_in'): return redirect(url_for('login'))
    return redirect(url_for('index'))
@app.route('/delete/<website>')
def delete(website):
    if not session.get('logged_in'): return redirect(url_for('login'))
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True, port=8080)