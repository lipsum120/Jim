from typing import List
from pydantic import BaseModel
from schemas.exercise_muscle import ExerciseRef
from schemas.types import NonEmpatyStr
    
class Muscle(BaseModel):
    id: int
    name: NonEmpatyStr
    exercises: List[ExerciseRef] = []
    
    model_config = {"from_attributes": True}
    
class MuscleCreate(BaseModel):
    name: NonEmpatyStr
    
class MuscleUpdate(BaseModel):
    name: NonEmpatyStr | None = None