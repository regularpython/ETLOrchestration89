from abc import ABC

from pydantic import BaseModel


class InputEventMessageABC(BaseModel, ABC):
    pass
