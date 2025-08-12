from src.mappers.orm_registry import run_mappers
from src.models.order_model import OrderModel
from src.repositories.order_repository import OrderRepository
run_mappers()


order = OrderModel(
    order_id='model test 2',
    user_id='sai 1234',
    total_amount=123.0,
    payment_method='creditcard',
    status="complete"
)



order_repo = OrderRepository()
order_repo.insert(order)
