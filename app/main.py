from fastapi import FastAPI, Header, Request, status
from fastapi.exceptions import RequestValidationError

from app.routers.index import router

app = FastAPI()
app.include_router(router)
