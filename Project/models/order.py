from . import db
from sqlalchemy import Integer, ForeignKey, DateTime, DECIMAL, func, Float
from sqlalchemy.orm import relationship

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.mapped_column(Integer, primary_key=True)
    user_id = db.mapped_column(Integer, db.ForeignKey('user.id'))
    date_created = db.mapped_column(DateTime)
    date_completed = db.mapped_column(DateTime, nullable=True)
    amount = db.mapped_column(Float, nullable=False)

    user = relationship("User", back_populates="orders")
    items = relationship("Orderbook", back_populates="order")
