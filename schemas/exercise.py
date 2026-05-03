from typing import List
from pydantic import BaseModel
from core.enums import ExerciseType
from schemas.exercise_muscle import MuscleRef


    
class Exercise(BaseModel):
    id: int
    name: str
    instruction: str
    exercise_types: ExerciseType
    muscles: List[MuscleRef] = []
    
    model_config = {"from_attributes": True}