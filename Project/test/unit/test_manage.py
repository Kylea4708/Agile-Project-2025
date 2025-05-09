import pytest
from app import app, db
from models import Genre
from manage import get_or_create_genre, fetch_books
from unittest.mock import patch

def test_get_or_create_genre_creates_new(test_client): # genre gets created if missing
    with test_client.application.app_context():
        genre = get_or_create_genre("Science Fiction")
        assert genre.name == "Science Fiction"

        retrieved = db.session.get(Genre, genre.id)
        assert retrieved is not None
        assert retrieved.name == "Science Fiction"


@patch("manage.requests.get")
def test_fetch_books_returns_mocked_data(mock_get): # Mocked API
    mock_get.return_value.json.return_value = {
        "items": [
            {"Book Information": {"title": "Mocked Book", "authors": ["Test Author"]}}
        ]
    }

    books = fetch_books("romance", max_results=1)

    assert isinstance(books, list)
    assert "Book Information" in books[0]
    assert books[0]["Book Information"]["title"] == "Mocked Book"