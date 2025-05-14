from . import db
from sqlalchemy import Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

class Orderbook(db.Model):  # renamed to match your __all__ import
    __tablename__ = 'orderbook'

    book_id = db.mapped_column(ForeignKey("book.id"), primary_key=True)
    order_id = db.mapped_column(ForeignKey("orders.id"), primary_key=True)
    quantity = db.mapped_column(Integer, nullable=False)
    unit_price = db.mapped_column(Float, nullable=False)

    book = relationship("Book", back_populates="order_items")
    order = relationship("Order", back_populates="items")