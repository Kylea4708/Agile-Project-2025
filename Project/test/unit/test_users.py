import pytest
from app import app, db
from models import User

def test_user_in_table(): #tests that the user values will be viewed on the table
    user = User(
        id = 1,
        name = "Test",
        phone = "574-824-9133"
    )

    assert user.id == 1
    assert user.name == "Test"
    assert user.phone == "574-824-9133"

def test_user_null_name():
    user = User(
        id = 1,
        phone = "574-824-9133"
    )

    assert user.name is None

def test_user_null_phone():
    user = User(
        id = 1,
        name = "Test",
    )

    assert user.phone is None

def test_id_is_int():
    user = User(
        id = "1"
    )

    assert user.id != int()

    with pytest.raises(TypeError):
        user.id("2")