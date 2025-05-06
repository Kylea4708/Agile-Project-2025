
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

✅ **May 6, 2025**
- Implemented dynamic book pricing based on genre and format (physical vs. digital)
- Replaced static order pricing with logic that derives unit price from genre-specific pricing tables
- Integrated boolean-to-format mapping using `True: "physical", False: "digital"` dictionary for cleaner logic
- Cleaned up order processing logic by removing unnecessary conditionals and using structured lookup
- Genre name matching made case-insensitive for consistent pricing resolution

✅ **May 3, 2025**
- Added search bars to both `books.html` and `readers.html` templates
- Implemented route-level filtering logic to support keyword-based search for:
  - Book titles and authors (case-insensitive match)
  - Reader names and phone numbers
- Ensured compatibility with existing pagination and list rendering
- Enhanced UX by preserving search input values after query execution

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

change thing