import unittest
from ..models.genre import Genre, Book

class TestGenreModel(unittest.TestCase):

    def test_genre_model_attributes(self):
        genre = Genre(name="Science Fiction")
        self.assertEqual(genre.name, "Science Fiction")

    def test_genre_books_relationship(self):
        genre = Genre(name="Fantasy")
        book1 = Book(title="Book 1", author="Author 1", quantity=3, physical=True, genre=genre)
        book2 = Book(title="Book 2", author="Author 2", quantity=4, physical=False, genre=genre)

        self.assertEqual(len(genre.books), 2) 
        self.assertEqual(genre.books[0].title, "Book 1")
        self.assertEqual(genre.books[1].title, "Book 2")

if __name__ == '__main__':
    unittest.main()