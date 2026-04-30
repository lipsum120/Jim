from fastapi import FastAPI
from api.v1.user import router

app = FastAPI()

app.include_router(router)