from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class OrderModel:
    order_id: str
    user_id: str
    total_amount: float
    payment_method: str
    status: str = "pending"
    created_at: datetime = None
    updated_at: datetime = None
