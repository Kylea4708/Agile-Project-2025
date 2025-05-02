from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
#from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from pathlib import Path
#from dotenv import load_dotenv
from db import db
from models import Book, User, Order, Orderbook
import os

# Load environment variables (if needed)
#load_dotenv()

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
# login_manager = LoginManager()
# login_manager.login_view = "login"
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return db.session.get(User, int(user_id))

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

@app.route("/order/new", methods=["GET", "POST"])
def admin_create_order():
    if request.method == "POST":
        user_id = int(request.form["user_id"])
        book_id = int(request.form["book_id"])
        quantity = int(request.form["quantity"])

        user = db.session.get(User, user_id)
        book = db.session.get(Book, book_id)

        if not user or not book:
            return "User or Book not found", 404

        amount = 10.0 * quantity  

        order = Order(user=user, amount=amount, date_created=datetime.now())
        order_item = Orderbook(book=book, quantity=quantity)
        order.items.append(order_item)

        db.session.add(order)
        db.session.commit()

        return redirect(url_for("orders"))  

   
    users = db.session.execute(db.select(User)).scalars().all()
    books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("admin_order.html", users=users, books=books)

if __name__ == "__main__":
    app.run(debug=True, port=8888)
