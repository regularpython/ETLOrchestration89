# src/repositories/order_item_repository.py
from sqlalchemy.orm import Session

from src.models.inventory_model import InventoryModel
from src.source.Database.database_connection import SESSION_FACTORY


class InventoryRepository:
    def __init__(self):
        self.session: Session = SESSION_FACTORY()

    # Insert Query
    def insert(self, item_details: InventoryModel) -> InventoryModel:

        self.session.add(item_details)
        self.session.commit()
        return item_details
