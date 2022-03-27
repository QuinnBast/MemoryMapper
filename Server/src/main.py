from fastapi import FastAPI
from endpoints import memory
from db.tables.memoryTable import Memory
from dependencies.dependencies import config, databaseProvider
import uvicorn

databaseProvider.create_tables()

app = FastAPI()
app.include_router(memory.router)


@app.get("/")
def read_root():
    memories = databaseProvider.get_session().query(Memory)
    return {"items": memories}


@app.get("/add")
def read_root():
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


if __name__ == '__main__':
    uvicorn.run(app, port=config.port, host='localhost')
