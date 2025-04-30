from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from pathlib import Path
from dotenv import load_dotenv
from db import db
from models import Book, User, Order
import os

# Load environment variables (if needed)
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book_store.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or "fallback-secret-key"

# DB setup
app.instance_path = Path(".").resolve()
db.init_app(app)
with app.app_context():
    db.create_all()

# Login Manager setup
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# --- Routes ---

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/books")
def books():
    books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("books.html", books=books)

@app.route("/users")
def users():
    users = db.session.execute(db.select(User)).scalars().all()
    return render_template("users.html", users=users)


@app.route("/orders")
def orders():
    orders = db.session.execute(db.select(Order)).scalars().all()
    return render_template("orders.html", orders=orders)



if __name__ == "__main__":
    app.run(debug=True, port=8888)
