from flask import Flask, render_template
from models.user import User
from database import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/create_db", methods=["GET"])
def create_db():
    return "Banco de dados criado com sucesso!"

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)