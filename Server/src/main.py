from fastapi import FastAPI
from endpoints import memory
from dependencies.dependencies import config, databaseProvider, cors
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

databaseProvider.create_tables()

app = FastAPI()
app.include_router(memory.router)

app.add_middleware(
   CORSMiddleware,
   allow_origins=cors.origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)


@app.get("/")
async def healthCheck():
    return {"active": True}


if __name__ == '__main__':
    uvicorn.run(app, port=config.port, host='0.0.0.0')
