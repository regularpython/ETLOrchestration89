from src.services.inventory_reserved_service import InventoryReservedEventService
from src.services.order_service import OrderService


class Workflow:
    def __init__(self):
        self.services = []

    def register_service(self, service):
        self.services.append(service)

    def get_service(self, service_name):
        for service in self.services:
            if service_name == service.name:
                print(service.name, service)
                return service
        raise Exception(f'{service_name} Service not found')

if __name__ == '__main__':
    work = Workflow()
    work.register_service(InventoryReservedEventService(''))
    work.register_service(OrderService(''))

    work.get_service('orderPlacedEvt')
