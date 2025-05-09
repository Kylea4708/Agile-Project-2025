from app import db
from models import Book, User
    
def test_booksearch_correct_title(test_client):
    with test_client.application.app_context():
        db.session.add(Book(title="Flask for Beginners", author="Ben", quantity=10, physical=True))
        db.session.add(Book(title="Video Game Guide", author="Mint", quantity=3, physical=False))
        db.session.commit()

    response = test_client.get("/books?q=Flask")
    html = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "Flask for Beginners" in html
    assert "Video Game Guide" not in html    

def test_user_correct_name(test_client):
    with test_client.application.app_context():
        db.session.add(User(name="Ben", phone="101-101-1010"))
        db.session.add(User(name="Dan", phone="999-999-9999"))
        db.session.commit()

    response = test_client.get("/users?q=Ben")
    html = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "Ben" in html
    assert "Dan" not in html 

def test_user_correct_number(test_client):
    with test_client.application.app_context():
        db.session.add(User(name="Ben", phone="101-101-1010"))
        db.session.add(User(name="Dan", phone="999-999-9999"))
        db.session.commit()

    response = test_client.get("/users?q=101-101-1010")
    html = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "Ben" in html
    assert "Dan" not in html 

def test_invalid_booksearch_title(test_client): # Checks if No books show up you don't enter anything
    with test_client.application.app_context():
        db.session.add(Book(title="Dune", author="Herbert", quantity=2, physical=True))
        db.session.commit()

    response = test_client.get("/books?q=")
    html = response.data.decode("utf-8")

    assert "Dune" not in html

def test_invalid_usersearch(test_client): # Checks for case-sensitivity
    with test_client.application.app_context():
        db.session.add(User(name="Ben", phone="101-101-1010"))
        db.session.commit()

    response = test_client.get("/books?q=BEN")
    html = response.data.decode("utf-8")

    assert "Ben" in html
    