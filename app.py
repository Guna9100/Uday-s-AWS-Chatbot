
from flask import Flask, request, render_template_string, redirect, url_for, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'guna-secret-key'

users = {
    "guna": "1234",
    "uday": "5678"
}

faq = {
    "what is ec2": "Amazon EC2 provides secure, resizable compute capacity in the cloud.",
    "what is s3": "Amazon S3 is a storage service used to store and retrieve any amount of data.",
    "what is lambda": "AWS Lambda lets you run code without provisioning or managing servers.",
    "who are you": "I am a chatbot created for a CSE project using AWS!",
    "who created you": "I was created by Guna using Flask and AWS services."
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect('/chat')
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get('username')
        pword = request.form.get('password')
        if uname in users and users[uname] == pword:
            session['username'] = uname
            return redirect('/chat')
        return "Invalid username or password. <a href='/login'>Try again</a>"
    return render_template_string(open("login.html").read())

@app.route('/chat')
def chat_page():
    if 'username' not in session:
        return redirect('/login')
    return render_template_string(open("chat.html").read())

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/chat_api')
def chat_api():
    if 'username' not in session:
        return "Unauthorized", 401
    message = request.args.get("message", "").lower()
    for keyword, answer in faq.items():
        if keyword in message:
            return answer
    return "Sorry, I don't understand that."
