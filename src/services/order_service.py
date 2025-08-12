import json
import uuid

from src.framework.etl_abstracts.orchesrtration_abstract import ETLOrchestratorBase
from src.models.order_model import OrderModel
from src.repositories.order_repository import OrderRepository
from src.schema.order_details_input_validator import OrderDetails
from src.utils.log_util import logger


class OrderService(ETLOrchestratorBase):
    name = 'orderPlacedEvent'

    def __init__(self, service_name, description):
        self.service_name = service_name,
        self.description = description
        self.service_id = str(uuid.uuid4())
        self.event = None
        self.order = None
        logger.info(
            f"[{self.name}] Service Initialized - ID: {self.service_id}, Name: {self.service_name}, Description: {self.description}")

    def validate_data(self):
        body = json.loads(self.event['Records'][0]['body'])
        self.order = OrderDetails(**body)

    def process_data(self):
        order_id = self.order.body.order_id
        user_id = self.order.body.user_id
        total_amount = self.order.body.total_amount
        payment_method = self.order.body.payment_method
        status = self.order.body.status

        # Data save
        order = OrderModel(
            order_id=order_id,
            user_id=user_id,
            total_amount=total_amount,
            payment_method=payment_method,
            status=status
        )

        order_repo = OrderRepository()
        order_repo.insert(order)


    def send_to_sqs(self):
        print('Not required')

    def process_the_event(self, event_data):
        logger.info(f"[{self.name}] Service Initialized - ID: {self.service_id} Received Event event: {event_data}")
        self.event = event_data