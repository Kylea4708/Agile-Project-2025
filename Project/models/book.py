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

   