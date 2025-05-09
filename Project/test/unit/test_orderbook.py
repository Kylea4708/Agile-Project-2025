import pytest
from datetime import datetime
from models import Orderbook

# tests a regular order
def test_orderbook():
    book_order = Orderbook (
        book_id = 1,
        order_id = 1,
        quantity = 5
    )

    assert book_order.book_id == 1
    assert book_order.order_id == 1
    assert book_order.quantity == 5


# test nullable quantity for book order
def test_nullable_quantity():
    orderbook = Orderbook (
        quantity = None
    )

    assert orderbook.quantity is None 

    with pytest.raises(TypeError):
        orderbook.quantity(None)
        

# test a negative quantity
def test_invalid_quantity():
    orderbook = Orderbook (
        quantity = -1
    )

    assert orderbook.quantity < 0 

    with pytest.raises(TypeError):
        orderbook.quantity(-1)


# missing book id
def test_null_book_id():
    orderbook = Orderbook (
        book_id = None
    )

    assert orderbook.book_id is None

    with pytest.raises(TypeError):
        orderbook.book_id(None)

# missing book id
def test_null_order_id():
    orderbook = Orderbook (
        order_id = None
    )

    assert orderbook.order_id is None

    with pytest.raises(TypeError):
        orderbook.order_id(None)