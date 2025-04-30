from . import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.mapped_column(Integer, primary_key=True)
    type = db.mapped_column(String)

    books = relationship("Book", back_populates="genre")