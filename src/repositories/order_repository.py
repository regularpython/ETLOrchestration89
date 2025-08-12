from sqlalchemy.orm import Session

from src.models.order_model import OrderModel
from src.source.Database.database_connection import SESSION_FACTORY


class OrderRepository:
    def __init__(self):
        self.session = SESSION_FACTORY() # Database connection

    # Insert Query
    def insert(self, order_detials: OrderModel):
        self.session.add(order_detials) # Insert query generatee
        self.session.commit() # Insert query execution
        return order_detials

    # Select all query
    def get_all(self):
        return self.session.query(OrderModel).all()
