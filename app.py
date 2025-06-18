from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return 'Welcome to the Secure App'

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'admin' and password == 'password123':
        app.logger.info(f"Successful login attempt by user: {username}")
        return 'Login Successful', 200
    else:
        app.logger.warning(f"Failed login attempt by user: {username}")
        return 'Login Failed', 401

if __name__ == '__main__':
    app.run()
