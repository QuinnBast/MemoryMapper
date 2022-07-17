from pydantic import BaseModel


class CreateMemoryRequest(BaseModel):
    memoryName: str
    memoryDescription: str

class CreateMomentRequest(BaseModel):
    momentFileData: str
    momentLocation: str
    momentDate: int
    momentDescription: str