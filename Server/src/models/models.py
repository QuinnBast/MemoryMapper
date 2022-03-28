from pydantic import BaseModel


class CreateMemoryRequest(BaseModel):
    memoryName: str
    memoryDescription: str
