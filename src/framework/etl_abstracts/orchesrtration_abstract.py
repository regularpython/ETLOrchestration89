# etl_orchestrator_base.py

from abc import ABC, abstractmethod
import boto3
import json


class ETLOrchestratorBase(ABC):


    @abstractmethod
    def validate_data(self):
        """Validate incoming data"""
        pass

    @abstractmethod
    def process_data(self):
        """Transform/process the data"""
        pass

    @abstractmethod
    def send_to_sqs(self):
        """Send message to SQS queue"""
        pass