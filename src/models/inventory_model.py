# models/order_item_model.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class InventoryModel:
    id: Optional[int] = None
    order_id: Optional[str] = None
    sku: str = ""
    quantity: int = ""
