from typing import List
from pydantic import BaseModel
from schemas.exercise import ExerciseBase
from schemas.exercise_muscle import ExerciseRef


    
class Muscle(BaseModel):
    id: int
    name: str
    exercises: List[ExerciseRef] = []
    
    model_config = {"from_attributes": True}
        