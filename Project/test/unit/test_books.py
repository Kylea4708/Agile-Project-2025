import unittest
from models import Book

def test_book_model():
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

