# registry.py

from sqlalchemy.orm import registry

from src.models.inventory_model import InventoryModel
from src.models.order_model import OrderModel
from src.tables.inventroy_table import inventory_table
from src.tables.order_table import orders_table

# Create a registry object
mapper_registry = registry()


def run_mappers():
    # Map the CarRentals class to the car_rentals_table
    mapper_registry.map_imperatively(OrderModel, orders_table)
    mapper_registry.map_imperatively(InventoryModel, inventory_table)

