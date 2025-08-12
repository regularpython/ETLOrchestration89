from sqlalchemy import Table, Column, String, DECIMAL, DateTime, MetaData, text
from src.common import config

# Define the metadata
metadata = MetaData()

# Define the orders table
orders_table = Table(
    "orders",
    metadata,
    Column("order_id", String(20), primary_key=True),
    Column("user_id", String(20), nullable=False),
    Column("total_amount", DECIMAL(10, 2), nullable=False),
    Column("payment_method", String(20), nullable=False),
    Column("status", String(20), nullable=False, server_default=text("'pending'")),
    Column("created_at", DateTime, server_default=text("CURRENT_TIMESTAMP")),
    Column("updated_at", DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
)
