import json

from src.framework.etl_abstracts.orchesrtration_abstract import ETLOrchestratorBase
from src.models.inventory_model import InventoryModel
from src.repositories.inventory_repository import InventoryRepository
from src.schema.inventory_reserved_event_input_validator import InventoryReservedEvent
import uuid

from src.utils.log_util import logger


class InventoryReservedEventService(ETLOrchestratorBase):
    name = 'inventoryReservedEvent'

    def __init__(self, service_name, description):
        self.service_name = service_name,
        self.description = description
        self.service_id = str(uuid.uuid4())

        self.event = None
        self.inventory_data = None
        logger.info(f"[{self.name}] Service Initialized - ID: {self.service_id}, Name: {self.service_name}, Description: {self.description}")

    def validate_data(self):


        body = json.loads(self.event['Records'][0]['body'])
        self.inventory_data = InventoryReservedEvent(**body)
        logger.info(f"[{self.name}] Service Initialized - ID: {self.service_id} Validated the data success")

    def process_data(self):
        repo = InventoryRepository()
        order_id = self.inventory_data.body.order_id
        items = self.inventory_data.body.reserved_items
        for item in items:
            data = InventoryModel(order_id=order_id, sku=item.sku, quantity=item.quantity)
            repo.insert(data)

    def send_to_sqs(self):
        pass

    def process_the_event(self, event_data):
        logger.info(f"[{self.name}] Service Initialized - ID: {self.service_id} Received Event event: {event_data}")
        self.event = event_data
