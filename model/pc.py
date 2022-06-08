from pydantic import BaseModel, Field

class Command(BaseModel):
    command: str

class Health_response(BaseModel):
    status: str