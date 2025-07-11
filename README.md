# AWS Chatbot with User Login System

This project is a simple, beginner-friendly chatbot built using **Python Flask**, hosted on **AWS EC2**, and secured with a basic **user login system**.

Users can log in and ask AWS-related questions through a clean HTML-based interface. The backend uses keyword matching to return predefined answers about AWS services.

---

## 🔧 Technologies Used

- **Python 3**
- **Flask** (Web framework)
- **Flask-Session** (for login sessions)
- **Flask-CORS** (to allow frontend-backend communication)
- **HTML + JavaScript** (Frontend)
- **AWS EC2 (Ubuntu)** – to host the app

---

## 🚀 How to Run This Project

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt


Step 2: Run Flask App
python3 app.py


Step 3: Open in Browser
Go to: http://<your-ec2-ip>:5000
Login using:
Username: guna
Password: 1234
