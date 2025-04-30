from . import db
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship

class Orderbook(db.Model):  # renamed to match your __all__ import
    __tablename__ = 'orderbook'

    book_id = db.mapped_column(ForeignKey("book.id"), primary_key=True)
    order_id = db.mapped_column(ForeignKey("orders.id"), primary_key=True)
    quantity = db.mapped_column(Integer, nullable=False)

    book = relationship("Book")
    order = relationship("Order", back_populates="items")