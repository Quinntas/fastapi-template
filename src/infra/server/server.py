from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware

from src.infra.database.mysql.mysql_connection import db
from src.infra.routers.v1_router import v1_router
from src.modules.shared.http.middleware.api_headers import ApiHeaders
from src.modules.shared.http.middleware.handle_exception import HandleException
from src.modules.shared.http.middleware.process_time import ProcessTimeMiddleware

app = FastAPI(
    title="FastAPI - Template",
    description="Template for FastAPI projects",
    version="0.1",
    contact={
        "name": "Caio Quintas",
        "email": "caioquintassantiago@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
    terms_of_service="MIT"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(ApiHeaders)
app.add_middleware(ProcessTimeMiddleware)
app.add_middleware(HandleException)

app.include_router(v1_router, prefix="/api/v1")


@app.on_event('startup')
async def startup():
    print("[Server] Server has started")


@app.on_event('shutdown')
async def shutdown():
    db.close()
    print("[Server] Server has stopped")
