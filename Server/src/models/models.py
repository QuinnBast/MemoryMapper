from pydantic import BaseModel
from datetime import datetime


class CreateMemoryRequest(BaseModel):
    latitude: int
    longitude: int
    memoryName: str
    date: datetime
