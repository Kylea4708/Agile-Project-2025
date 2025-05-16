import sys
from pathlib import Path

import pytest

# Add Project directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Now use absolute imports
from app import app, db
from models import Book, User, Genre

@pytest.fixture
def client():
    # Configure the app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    # Create test client
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            
            # Create test data
            genre = Genre(name="Fiction")
            db.session.add(genre)
            
            book = Book(title="Python 101", author="John Doe", genre=genre, quantity=10, physical=True)
            db.session.add(book)
            
            user = User(name="John Doe", phone="123-456-7890")
            db.session.add(user)
            
            book1 = Book(title="Test 101", author="Luke Skywalker", genre=genre, quantity=20, physical=False)
            db.session.add(book1)

            user1 = User(name="Jenny Smith", phone="(123) 456-7890")
            db.session.add(user1)

            db.session.commit()
        yield client
    
    # Clean up after tests
    with app.app_context():
        db.drop_all()