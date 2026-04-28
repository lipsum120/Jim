from fastapi import FastAPI
from core.init_db import init_db

app = FastAPI()

init_db()