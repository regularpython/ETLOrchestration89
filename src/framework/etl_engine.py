import json

from src.framework.workflow.workflow_service import Workflow


class Engine:
    def __init__(self, workflow: Workflow):
        self.workflow = workflow

    def execute(self, event):
        event_name = json.loads(event['Records'][0]['body'])['header']['eventName']
        service = self.workflow.get_service(event_name)
        service.process_the_event(event)
        service.validate_data()
        service.process_data()
        service.send_to_sqs()