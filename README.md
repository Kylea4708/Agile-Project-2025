
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

## 🛠️ How to Use the Project
### 1. Install dependencies

Make sure you have Python 3.10+ and run on your terminal:

`pip install -r requirements.txt`

### 2. Run the Flask app

From the project directory, `cd  Project`:

`python manage.py run`

### 3. Import demo data (optional):

`python manage.py import-users`
`python manage.py create-books`

### 4. Navigate the app

Open a browser and run:

`python app.py`


The address the app is set to is:
http://127.0.0.1:8888


**Have fun!**

---

Key Features:

📘 Books: View, search, filter, and sort the catalog

👥 Users: Search by name or phone, sort alphabetically

📦 Orders: View and create new orders (admin)

🔍 Search: Supports flexible formats (e.g., phone numbers with or without punctuation)



## 🆕 Recent Changes

✅ **May 20, 2025**
- Enhanced `/users` search functionality to support flexible phone number formatting:
  - Now accepts input with dashes, parentheses, or spaces (e.g., `1234567890`, `(123) 456-7890`)
  - Implemented digit normalization using SQLAlchemy's `func.replace`
- Improved SQL filter logic using `or_(*filters)` and helper functions
- Added defensive checks to avoid query crashes due to empty search fields

✅ **May 16, 2025**
- Added `sort A–Z` and `sort Z–A` buttons to `books.html` and `users.html`
- Implemented alphabetical sorting using SQLAlchemy's `order_by()` with `asc()` and `desc()`
- Sorting is maintained alongside search and filter results
- UI improvements: separated sort buttons from search filters for cleaner layout

✅ **May 9, 2025**
- Reintegrated user search filtering by both name and phone number
- Added Tests for the functionality of the project
- Fixed bugs related to blank queries and inconsistent matches in search bar

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

