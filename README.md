
# 📚 Agile Book Store Project

This is a Flask-based web application for managing books, readers, and orders in a digital library or book store environment. The project uses SQLAlchemy ORM for database models, Jinja2 templates for rendering HTML, and Bootstrap for styling.

---

## 🚀 Features

- View list of all books with genre and availability
- View registered readers
- View order history with amount and status
- Responsive UI styled with Bootstrap
- Modular structure with SQLAlchemy 2.0-style models
- Automatic database creation on first run

## 🆕 Recent Changes
✅ **May 7th, 2025**

✅ **April 30, 2025**
- Added relational `Book` and `Genre` models using `genre_id` foreign key
- Created `Reader`, `Order`, and `ProductOrder` models
- Refactored model imports to prevent circular dependencies (`from db import db`)
- Set up automatic table creation using `db.create_all()` on app start
- Built and styled the following HTML pages:
  - `books.html`, `readers.html`, `orders.html`
- Updated `home.html` to include buttons linking only to:
  - 📘 Books
  - 👥 Readers
  - 📦 Orders

Kyle, Dylan, Sandy, Arsh, Mario, and Maliyah

