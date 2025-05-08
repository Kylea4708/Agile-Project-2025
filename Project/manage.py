import csv
import random
import sys
from db import db
from app import app
from models import User, Book, Genre 
import requests
from sqlalchemy import select

def import_users():
    with app.app_context():
        with open('customers.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = User(
                    name=row['name'],
                    phone=row['phone']
                )
                db.session.add(user)
            db.session.commit()
            print(f"Imported {reader.line_num - 1} users.")

def fetch_books(subject, max_results=None):
    if max_results is None:
        max_results = random.randint(10,100)

    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"subject:{subject}", "maxResults": max_results}
    response = requests.get(url, params=params)
    return response.json().get("items", [])

def get_or_create_genre(name):
    genre = db.session.execute(select(Genre).filter_by(name=name)).scalar()
    if not genre:
        genre = Genre(name=name)
        db.session.add(genre)
        db.session.commit()
    return genre

def create_books():
    genres = [
        "fiction", "romance", "mystery", "history", "fantasy",
        "science", "poetry", "travel", "thriller", "biography"
    ]

    random_genre = random.choice(genres)
    print(f"Selected genre: {random_genre}")

    with app.app_context():
        db.create_all()
        books_data = fetch_books(random_genre)

        count = 0

        for item in books_data:
            volume = item.get("volumeInfo", {})
            title = volume.get("title")


            authors = ", ".join(volume.get("authors", ["Unknown Author"]))
            categories = volume.get("categories", [random_genre.capitalize()])
            genre_name = categories[0]

            genre = get_or_create_genre(genre_name)

            exists = db.session.execute(
                select(Book).filter_by(title=title, author=authors)
            ).scalar()

            if exists:
                print(f"Skipping duplicate: {title}")
                continue

            book = Book(
                title=title,
                author=authors,
                genre=genre,
                quantity=random.randint(10,100),
                physical=True
            )
            db.session.add(book)
            count += 1
            print(f"Added: {title} by {authors}")

        db.session.commit()
        print(f"{count}, books successfully added.")

def main():
    if len(sys.argv) < 2:
        print("Available commands:")
        print("  import-users  - Load customers.csv into User table")
        print("  create-books  - Fetch random genre and add books to DB")
        sys.exit(1)

    command = sys.argv[1]

    if command == "import-users":
        import_users()
    elif command == "create-books":
        create_books()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()