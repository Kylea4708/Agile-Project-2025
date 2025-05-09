import unittest
from models import Genre, Book


def test_genre_model_valid_input_values():
        # Test where a genre object is correctly initialized with input values
        genre = Genre(id = 1, 
                      name="Science Fiction")
        assert genre.name == "Science Fiction"
        assert genre.id == 1

    
def test_genre_model_empty_genre_name():
        # Test where genre name is empty
        genre = Genre(id = 1,
                      name="" )
        assert genre.name == ""


def test_genre_model_zero_genre_id():
        # Test where genre id is zero
        genre = Genre(id = 0,
                      name="Adventure")
        assert genre.id == 0


def test_genre_model_incorrect_datatype_for_genre_name():
        # Test where datatype is incorrect for genre name
        genre = Genre(id = 1,
                      name=1)
        assert isinstance(genre.name, str)


def test_genre_model_incorrect_datatype_for_id():
        # Test where datatype is incorrect for id
        genre = Genre(id = "1",
                      name="History")
        assert isinstance(genre.id, int)