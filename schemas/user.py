from typing import List
from pydantic import BaseModel
from schemas.workout import Workout


class User(BaseModel):
    id: int
    name: str
    height: float
    weight: float
    workouts: List[Workout] = []
    
    class Config:
        orm_mode: bool = True