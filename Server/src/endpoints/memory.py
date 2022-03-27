import uuid
from dependencies.dependencies import databaseProvider
from models.models import CreateMemoryRequest
from db.tables.memoryTable import Memory
from fastapi import APIRouter

router = APIRouter(
    prefix="/memory",
    tags=["memories"],
)


@router.put("/")
def save_memory(request: CreateMemoryRequest):
    memory = Memory(
        name="NewMemory",
        latitude=123123,
        longitude=123123,
        date=123123123
    )
    session = databaseProvider.get_session()
    session.add(memory)
    session.commit()
    out = []
    for row in session.query(Memory):
        out.append(row)
    return {"items": out}


@router.get("/{memory_id}")
def save_memory(memory_id: int):
    return {"id": memory_id}
