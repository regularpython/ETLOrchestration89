
from pydantic import BaseModel, field_validator
from typing import List

from src.common.constants import STATUS_TYPES


class Items(BaseModel):
    sku: str
    quantity: int


class OrderHeader(BaseModel):
    eventName: str
    publisher: str
    organizationId: str
    source: str
    timestamp: str


class OrderBody(BaseModel):
    order_id: str
    user_id: str
    items: List[Items]
    total_amount: float
    payment_method: str
    status: str

    @field_validator("status")
    @classmethod
    def check_age(cls, value):
        if value not in STATUS_TYPES:
            raise ValueError("status shold be a valid one")
        return value


class OrderDetails(BaseModel):
    header: OrderHeader
    body: OrderBody