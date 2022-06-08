from typing import Union
from pydantic import BaseModel

class Command(BaseModel):
    command: str
