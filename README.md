
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

---

## How to Use



## 🆕 Recent Changes

✅ **May 6, 2025**
- Implemented dynamic book pricing based on genre and format (physical vs. digital) using a genre-based pricing matrix
- Replaced static order pricing with logic that calculates unit price dynamically during order creation
- Integrated boolean-to-format mapping via `{ True: "physical", False: "digital" }` for clean format resolution
- Made genre key access case-insensitive to prevent lookup errors
- Added order detail view (`/orders/<id>`) to display all items, quantities, unit prices, and subtotals in a dedicated page
- Designed responsive "book-like" order cards using Bootstrap — each order appears as a visual tile and links to its details
- Deprecated tabular order layout in favor of a more engaging, card-based interface for browsing orders


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

