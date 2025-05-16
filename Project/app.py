from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from sqlalchemy import asc, desc, or_, func
from pathlib import Path
from db import db
from models import Book, User, Order, Orderbook, Genre
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
    search_query = request.args.get("q", "").strip()
    genre_filter = request.args.get("genre_filter")
    format_style = request.args.get("format_style")
    sort_order = request.args.get("sort", "")

    stmt = db.select(Book)

    if search_query:
        stmt = stmt.where(or_(Book.title.ilike(f"%{search_query}%"), Book.author.ilike(f"%{search_query}%")))
    
    if genre_filter and genre_filter.strip() != "":
        stmt = stmt.join(Book.genre).where(Genre.name == genre_filter)

    if format_style == 'physical':
        stmt = stmt.where(Book.physical == True)

    if format_style == 'digital':
        stmt = stmt.where(Book.physical == False)

    if sort_order == "asc":
        stmt = stmt.order_by(asc(Book.title))
    
    if sort_order == "desc":
        stmt = stmt.order_by(desc(Book.title))

    books = db.session.execute(stmt).scalars().all()

    genres = db.session.execute(db.select(Genre)).scalars().all()

    return render_template("books.html", books=books,search_query=search_query,genres=genres)

def only_digits(phone_string):
    return ''.join(filter(str.isdigit, phone_string))

@app.route("/users")
def users():
    search_query= request.args.get("q","").strip()
    sort_order = request.args.get("sort", "")

    stmt = db.select(User)

    if search_query:
        cleaned_digits = only_digits(search_query)
        
        stmt = stmt.where(or_(User.name.ilike(f"%{search_query}%"), func.replace(func.replace(func.replace(User.phone, '-', ''), '(', ''), ')', '').ilike(f"%{cleaned_digits}%")))
    
    if sort_order == "asc":
        stmt = stmt.order_by(asc(User.name))
    
    if sort_order == "desc":
        stmt = stmt.order_by(desc(User.name))

    users = db.session.execute(stmt).scalars().all()
    return render_template("users.html", users=users,search_query=search_query)


@app.route("/orders")
def orders():
    orders = db.session.execute(db.select(Order)).scalars().all()
    return render_template("orders.html", orders=orders)

@app.route("/orders/<int:order_id>/delete", methods=["POST"])
def delete_order(order_id):
    order = db.session.get(Order, order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
    return redirect(url_for("orders"))

@app.route("/orders/<int:order_id>")
def order_details(order_id):
    order = db.session.get(Order, order_id)

    items_with_subtotals = []
    total = 0

    for item in order.items:
        subtotal = item.unit_price * item.quantity
        total += subtotal
        items_with_subtotals.append({
            "title": item.book.title,
            "quantity": item.quantity,
            "price": item.unit_price,
            "subtotal": subtotal
        })

    return render_template("User_order.html", order=order, items=items_with_subtotals, total=total)

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

        price_per_book = random.randint(10, 50)
        amount = price_per_book * quantity

        order = Order(user=user, amount=amount, date_created=datetime.now())
        order_item = Orderbook(book=book, quantity=quantity, unit_price=price_per_book)
        order.items.append(order_item)

        db.session.add(order)
        db.session.commit()

        return redirect(url_for("orders"))  

   
    users = db.session.execute(db.select(User)).scalars().all()
    books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("admin_order.html", users=users, books=books)

@app.route("/manage-books", methods=["GET", "POST"])
def manage_books():
    if request.method == "POST":
        if "create" in request.form:
            title = request.form["title"]
            author = request.form["author"]
            genre_name = request.form["genre_name"] 
            quantity = int(request.form["quantity"])
            physical = bool(request.form.get("physical", False))

            genre = db.session.execute(db.select(Genre).filter_by(name=genre_name)).scalar()
            if not genre:
                genre = Genre(name=genre_name)
                db.session.add(genre)
                db.session.commit()

            book = Book(
                title=title,
                author=author,
                genre=genre,
                quantity=quantity,
                physical=physical
            )
            db.session.add(book)
            db.session.commit()

        elif "edit" in request.form:
            book_id = int(request.form["book_id"])
            book = db.session.get(Book, book_id)
            if book:
                book.title = request.form["title"]
                book.author = request.form["author"]
                book.genre_id = int(request.form["genre_id"])
                book.quantity = int(request.form["quantity"])
                book.physical = bool(request.form.get("physical", False))
                db.session.commit()

        elif "delete" in request.form:
            book_id = int(request.form["book_id"])
            book = db.session.get(Book, book_id)
            if book:
                affected_orders = {item.order for item in book.order_items}
        
                db.session.delete(book)
                db.session.commit()

                for order in affected_orders:
                    if not order.items:  
                        db.session.delete(order)
        
        db.session.commit()

        return redirect(url_for("manage_books"))

    genres = db.session.execute(db.select(Genre)).scalars().all()
    books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("manage_books.html", books=books, genres=genres)


if __name__ == "__main__":
    app.run(debug=True, port=8888)
