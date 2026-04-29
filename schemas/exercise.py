from ast import List
from pydantic import BaseModel
from core.enums import ExerciseType
from schemas.muscle import Muscle


class Exercise(BaseModel):
    id: int
    name: str
    instruction: str
    exercise_types: ExerciseType
    muscles: List[Muscle] = []
    
    class Config:
        orm_mode: bool = True
    