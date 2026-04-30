from typing import List
from pydantic import BaseModel
from core.enums import ExerciseType


class Exercise(BaseModel):
    id: int
    name: str
    instruction: str
    exercise_types: ExerciseType
    # muscles: List["Muscle"] = []
    
    # class Config:
    #     orm_mode = True
    
    