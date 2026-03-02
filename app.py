from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def home():
    return "MVP DevSecOps - Aplicacion en Docker"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    logging.info(f"Intento de login - Usuario: {username} - Password: {password}")

    if username == "admin" and password == "1234":
        return "Login exitoso"
    else:
        return "Credenciales incorrectas", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)