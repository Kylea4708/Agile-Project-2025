import pytest
from models import Order
from datetime import datetime

# tests regular order
def test_order():
    order = Order(
        id = 1,
        user_id = 1, 
        amount = 100.99, 
        date_created = datetime.now()
        )

    assert order.id == 1
    assert order.user_id == 1
    assert order.amount == 100.99


# test nullable date
def test_nullable_date():
    order = Order (
        user_id = 2,
        amount = 249.99,
    )
    
    assert order.date_completed is None
    

# amount cannot be nullable
def test_null_amount():
    order = Order (
        amount = None
    )

    assert order.amount is None

    with pytest.raises(TypeError):
        order.amount(None)


# testing an amount that is negative 
def test_negative_amount():
    order = Order (
        amount = -2
    )

    assert order.amount < 0

    with pytest.raises(TypeError):
        order.amount(-1)


# tests for type error when id is not an integer
def test_id_is_int():
    order = Order (
        id = "1"
    )

    assert order.id != int()

    with pytest.raises(TypeError):
        order.id("2")


# when user id is not an int
def test_userid_is_int():
    order = Order (
        user_id = "1"
    )

    assert order.user_id != int()

    with pytest.raises(TypeError):
        order.id("1")