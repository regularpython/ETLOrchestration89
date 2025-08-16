from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from src.common import config

# Define the metadata
metadata = MetaData()

# Define the order_items table
inventory_table = Table(
    "order_items",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("order_id", String(20), nullable=True),
    Column("sku", String(20), nullable=False),
    Column("quantity", String(45), nullable=False),
)
