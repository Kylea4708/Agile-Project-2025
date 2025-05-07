import pytest
from app import app, db
from models import Book, User

@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        db.drop_all()
    
def test_booksearch_correct_title(test_client):
    with app.app_context():
        db.session.add(Book(title="Flask for Beginners", author="Ben", quantity=10, physical=True))
        db.session.commit()

    response = test_client.get("/books?q=flask")
    assert response.status_code == 200
    assert b"Flask for Beginners" in response.data
    assert b"Video Game Guide" not in response.data
