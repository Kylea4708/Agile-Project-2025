from . import db
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Book(db.Model):
    __tablename__ = 'book'

    id = db.mapped_column(Integer, primary_key=True)
    title = db.mapped_column(String)
    author = db.mapped_column(String)
    quantity = db.mapped_column(Integer, default=0)
    physical = db.mapped_column(Boolean, default=False)
    genre_id = db.mapped_column(Integer, ForeignKey('genre.id'))

    genre = relationship("Genre", back_populates="books")

    def __init__(self, id, title, author, quantity=0, physical=False, genre_id=None):
        if not isinstance(id, int):
            raise TypeError("id must be an int")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not isinstance(author, str):
            raise TypeError("author must be a string")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an int")
        if not isinstance(physical, bool):
            raise TypeError("physical must be a boolean")
        if genre_id is not None and not isinstance(genre_id, int):
            raise TypeError("genre_id must be an int if provided")

        if quantity < 0:
            quantity = 0  # or raise ValueError if needed
        if genre_id is not None and genre_id < 0:
            genre_id = 0  # or raise ValueError if needed

        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.physical = physical
        self.genre_id = genre_id
