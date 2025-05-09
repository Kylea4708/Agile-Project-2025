import unittest
from models import Book
import pytest


def test_book_model_valid_input_values():
    # Test where a book object is correctly initialized with input values
    book = Book(
        id =1,
        title="George Mills", 
        author="Stanley Elkin", 
        quantity=5, 
        physical=True, 
        genre_id=1)
    
    assert book.id == 1
    assert book.title == "George Mills"
    assert book.author == "Stanley Elkin"
    assert book.quantity == 5
    assert book.physical == True
    assert book.genre_id == 1


def test_book_model_negative_quantity():
        # Test where book quantity is zero
        book = Book(id=2, title="A Night In Paris", author="Dov Alfon", quantity=-10, physical=False, genre_id=2)
        assert book.quantity >= 0


def test_book_model_empty_title():
        # Test where book title is missing
    with pytest.raises(ValueError):
        book = Book(id=4, title="", author="Unknown", quantity=1, physical=True, genre_id=4)


def test_book_model_empty_author():
        # Test where book author is missing
    with pytest.raises(ValueError):
        book = Book(id=6, title="Mill On The Po", author="", quantity=1, physical=False, genre_id=5)


def test_book_model_large_quantity():
        # Test where book quantity is large
        large_quantity = 10**6
        book = Book(id=7, title="Clockwork Orange", author="Anthony Burgess", quantity=large_quantity, physical=False, genre_id=6)
        assert book.quantity == large_quantity


def test_book_model_physical_is_true():
        # Test where book is digital (physical is False)
        book = Book(id=8, title="Ithaca Forever", author="Luigi Malerba", quantity=10, physical=True, genre_id=7)
        assert book.physical 


def test_book_model_negative_genre_id():
       # Test where book genre id is negative
       book = Book(id=9, title="Doppelganger", author="G.F. Heard", quantity=20, physical=False, genre_id=-10)
       assert book.genre_id >= 0


def test_book_model_incorrect_datatype_for_id():
        # Test where datatype is incorrect for id field
    with pytest.raises(TypeError):
        book = Book(id="9", title="Julie", author="Jacques Rousseau", quantity=20, physical=False, genre_id=-10)
        

def test_book_model_incorrect_datatype_for_title():
        # Test where datatype is incorrect for title field
    with pytest.raises(TypeError):
       book = Book(id=9, title=12345, author="Mary Timon", quantity=20, physical=False, genre_id=-10)


def test_book_model_incorrect_datatype_for_author():
        # Test where datatype is incorrect for author field
    with pytest.raises(TypeError):
       book = Book(id=9, title="hopeful", author=67, quantity=20, physical=False, genre_id=-10)
       

def test_book_model_incorrect_datatype_for_quantity():
        # Test where datatype is incorrect for quantity field
    with pytest.raises(TypeError):
       book = Book(id="9", title="Time Shelter", author="Georgi Gospodinov", quantity="20", physical=False, genre_id=-10)


def test_book_model_incorrect_datatype_for_genre_id():
        # Test where datatype is incorrect for genre_id field
    with pytest.raises(TypeError):
       book = Book(id="9", title="Ivanhoe", author="Walter Scott", quantity=20, physical=False, genre_id="10")