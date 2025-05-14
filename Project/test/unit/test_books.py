import pytest
from models import Book

# test regular book

def test_book():
    book = Book (
        id = 2,
        title = "Title",
        author = "Author",
        quantity = 3,
        physical = False,
        genre_id = 2
    )

    assert book.id == 2
    assert book.title == "Title"
    assert book.author == "Author"
    assert book.quantity == 3
    assert book.physical == False
    assert book.genre_id == 2

# id is not an int
def test_id_not_int():
    book = Book (
        id = "1"
    )

    assert book.id != int()

    with pytest.raises(TypeError):
        book.id("1")

# test no author
def test_missing_author():
    book = Book (
        author = None
    )

    assert book.author is None

    with pytest.raises(TypeError):
        book.author(None)

# tests invalid quantity
def test_invalid_quantity():
    book = Book (
        quantity = -1
    )

    assert book.quantity < 0

    with pytest.raises(TypeError):
        book.quantity(-2)

# test missing id 
def test_missing_id():
    book = Book (
        id = None
    )

    assert book.id is None

    with pytest.raises(TypeError):
        book.id(None)

# test missing title
def test_missing_title():
    book = Book (
        title = None
    )

    assert book.title is None

    with pytest.raises(TypeError):
        book.title(None)