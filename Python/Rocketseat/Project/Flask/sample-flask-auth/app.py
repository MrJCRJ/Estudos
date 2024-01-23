from flask import Flask, render_template, request, jsonify
from models.user import User
from database import db
from config import Config
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return jsonify({"message": "Autenticação realizada com sucesso"})

    return jsonify({"message":"Credenciais inválidas"}), 400

@app.route("/create_db", methods=["GET"])
def create_db():
    return "Banco de dados criado com sucesso!"

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)