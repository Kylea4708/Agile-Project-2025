from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from pathlib import Path
from db import db
from models import Book, User, Order, Orderbook
import os
import random



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book_store.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or "fallback-secret-key"


app.instance_path = Path(".").resolve()
db.init_app(app)
with app.app_context():
    db.create_all()



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/books")
def books():
    search_query = request.args.get("q","").strip()
    stmt = db.select(Book)
    if search_query:
        stmt = stmt.filter(Book.title.ilike(f"%{search_query}%"))

    books = db.session.execute(stmt).scalars().all()
    return render_template("books.html", books=books,search_query=search_query)

@app.route("/users")
def users():
    search_query= request.args.get("q","").strip()
    stmt = db.select(User)

    if search_query:
        stmt = stmt.filter(User.name.ilike(f"%{search_query}%"))
    
    users = db.session.execute(stmt).scalars().all()
    return render_template("users.html", users=users,search_query=search_query)


@app.route("/orders")
def orders():
    orders = db.session.execute(db.select(Order)).scalars().all()
    return render_template("orders.html", orders=orders)

@app.route("/order/new", methods=["GET", "POST"])
def admin_create_order():

    pricing = {
        "fiction": {"physical": random.uniform(15.00, 25.00), "digital": random.uniform(7.50, 12.50)}, 
        "romance": {"physical": random.uniform(8.00, 15.00), "digital":  random.uniform(4.00, 7.50)}, 
        "mystery": {"physical": random.uniform(14.00, 22.00), "digital":  random.uniform(7.00, 11.00)}, 
        "fantasy": {"physical": random.uniform(16.00, 28.00), "digital":  random.uniform(8.00, 14.00)},
        "science": {"physical": random.uniform(15.00, 26.00), "digital":  random.uniform(7.50, 13.00)}, 
        "history": {"physical": random.uniform(18.00, 30.00), "digital":  random.uniform(9.00, 15.00)}, 
        "biography": {"physical": random.uniform(18.00, 28.00), "digital":  random.uniform(9.00, 14.00)},
        "poetry": {"physical": random.uniform(12.00, 20.00), "digital":  random.uniform(6.00, 10.00)}, 
        "thriller": {"physical": random.uniform(13.00, 21.00), "digital":  random.uniform(6.50, 10.50)}, 
        "travel": {"physical": random.uniform(15.00, 27.00), "digital":  random.uniform(7.50, 13.50)}, 
    }

    format = {
        True: "physical",
        False: "digital",
    }

    if request.method == "POST":
        user_id = int(request.form["user_id"])
        book_id = int(request.form["book_id"])
        quantity = int(request.form["quantity"])

        user = db.session.get(User, user_id)
        book = db.session.get(Book, book_id)

        if not user or not book:
            return "User or Book not found", 404

        genrekey = book.genre.name.lower()
        formatkey = format[book.physical]
        priceofbook = pricing[genrekey][formatkey]

        amount = priceofbook * quantity

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
