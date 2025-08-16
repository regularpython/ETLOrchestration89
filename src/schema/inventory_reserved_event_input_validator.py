
from pydantic import BaseModel
from typing import List


class Items(BaseModel):
    sku: str
    quantity: str


class InventoryReservedHeader(BaseModel):
    eventName: str
    publisher: str
    organizationId: str
    source: str
    timestamp: str


class InventoryReservedBody(BaseModel):
    order_id: str
    reserved_items: List[Items]


class InventoryReservedEvent(BaseModel):
    header: InventoryReservedHeader
    body: InventoryReservedBody
