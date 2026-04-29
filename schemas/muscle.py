from typing import List
from pydantic import BaseModel
from schemas.exercise import Exercise


class Muscle(BaseModel):
    id: int
    name: str
    exercises: List[Exercise] = []
    
    class Config:
        orm_mode: bool = True