import json

from src.framework.etl_engine import Engine
from src.framework.workflow.workflow_service import Workflow
from src.mappers.orm_registry import run_mappers
from src.services.inventory_reserved_service import InventoryReservedEventService
from src.services.order_service import OrderService
run_mappers()

work = Workflow()
work.register_service(InventoryReservedEventService(service_name="Inventory Reserved Event", description="This stores inventory into database"))
work.register_service(OrderService(service_name="Order Event", description="This stores inventory into database"))
engine = Engine(work)


def lambda_handler(event, context):
    engine.execute(event)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
