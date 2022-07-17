from msilib import UuidCreate
import uuid
from dependencies.dependencies import databaseProvider
from models.models import CreateMemoryRequest, CreateMomentRequest
from db.tables.memoryTable import Memory, Moment
from fastapi import APIRouter

router = APIRouter(
    prefix="/memory",
    tags=["memories"],
)


@router.put("/")
def save_memory(request: CreateMemoryRequest):
    memory = Memory(
        name=request.memoryName,
        description=request.memoryDescription,
        position=None,
        startDate=None,
        endDate=None,
    )
    session = databaseProvider.get_session()
    session.add(memory)
    session.commit()
    out = []
    for row in session.query(Memory):
        out.append(row)
    return {"items": out}


@router.get("/")
def get_all_memories():
    session = databaseProvider.get_session()
    memories = []
    for row in session.query(Memory):
        memories.append(row)
    return {"items": memories}


@router.get("/{memory_id}")
def get_memory(memory_id: int):
    session = databaseProvider.get_session()
    for row in session.query(Memory).filter(Memory.id == memory_id):
        return row

@router.get("/{memory_id}/moments")
def get_moments(memory_id: int):
    session = databaseProvider.get_session()
    moments = []
    for row in session.query(Moment).filter(Moment.memory_id == memory_id):
        moments.append(row)
    return {"items": moments}

@router.put("/{memory_id}/moment")
def put_moment(memory_id: int, request: CreateMomentRequest):
    fileId = UuidCreate()

    moment = Moment(
        memory_id=memory_id,
        file_id=fileId,
        description=request.momentDescription,
        position=request.momentLocation,
        date=request.momentDate,
    )
    session = databaseProvider.get_session()
    session.add(moment)
    session.commit()
    return get_moments(memory_id)
