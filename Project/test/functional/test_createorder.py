from app import db
from models import Book, User

def test_creating_order(test_client):
    with test_client.application.app_context():
        user = User(name="tester", phone = "000-000-0000")
        book = Book(title="Flask for Beginners",  author="Ben", quantity=10, physical=True)

        db.session.add_all([user, book])
        db.session.commit()

    response = test_client.post("/order/new", data= {
        "user_id": 1,
        "book_id": 1,
        "quantity": 3
    }, follow_redirects=True)

    html = response.data.decode("utf-8")
    assert response.status_code == 200

    assert "Order" in html
    assert "Flask for Beginners" in html
    assert "tester" in html
    assert "$30.00" in html

def test_invalid_user_in_order(test_client): # If the there is an invalid user to an order displayed to the page
    with test_client.application.app_context():
        book = Book(title="Flask for Beginners",  author="Ben", quantity=10, physical=True)
    
        db.session.add(book)
        db.session.commit()
    
    response = test_client.post("/order/new", data= {
        "user_id": 999,
        "book_id": 1,
        "quantity": 3
    }, follow_redirects=True)

    assert response.status_code == 404
    html = response.data.decode("utf-8")

    assert "User or Book not found" in html

def test_invalid_book_in_order(test_client): # If the there is an invalid book in an order displayed to the page  
    with test_client.application.app_context():
        user = User(name="tester", phone = "000-000-0000")
    
        db.session.add(user)
        db.session.commit()
    
    response = test_client.post("/order/new", data= {
        "user_id": 1,
        "book_id": 999,
        "quantity": 3
    }, follow_redirects=True)

    assert response.status_code == 404
    html = response.data.decode("utf-8")

    assert "User or Book not found" in html

def test_invalid_book_in_order(test_client): # If the there is an invalid quantity in an order 
    with test_client.application.app_context():
        user = User(name="tester", phone = "000-000-0000")
        book = Book(title="Flask for Beginners",  author="Ben", quantity=10, physical=True)

        db.session.add_all([user, book])
        db.session.commit()
    
    response = test_client.post("/order/new", data= {
        "user_id": 1,
        "book_id": 999,
    }, follow_redirects=True)

    assert response.status_code == 400
    html = response.data.decode("utf-8")

    assert "Bad Request" in html