import pytest
from app import app, db
from models import User

@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

@pytest.fixture
def sample_users():
    user1 = User(name="Alice")
    user2 = User(name="Bob")
    db.session.add_all([user1, user2])
    db.session.commit()

def test_users_page_loads(test_client, sample_users):
    response = test_client.get("/users")
    assert response.status_code == 200
    assert b"Alice" in response.data
    assert b"Bob" in response.data

def test_user_search(test_client, sample_users):
    response = test_client.get("/users?q=Alice")
    assert response.status_code == 200
    assert b"Alice" in response.data
    assert b"Bob" not in response.data
