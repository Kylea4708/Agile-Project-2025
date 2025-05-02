from . import db
from sqlalchemy import Integer, String, func
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'user'

    id = db.mapped_column(Integer, primary_key=True)
    name = db.mapped_column(String)
    phone = db.mapped_column(String)

    orders = db.relationship("Order", back_populates='user')