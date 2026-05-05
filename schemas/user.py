from typing import List
from pydantic import BaseModel, Field, field_validator
from schemas.types import NonEmpatyStr
from schemas.workout import Workout


class User(BaseModel):
    id: int
    name: NonEmpatyStr
    height: float
    weight: float
    workouts: List[Workout] = []
    
    model_config = {"from_attributes": True}
    
class UserCreate(BaseModel):
    name: NonEmpatyStr
    height: float = Field(..., gt=0, lt=300)
    weight: float = Field(..., gt=0, lt=500)
    
class UserUpdate(BaseModel):
    name: NonEmpatyStr | None = None
    height: float | None = Field(None, gt=0, lt=300)
    weight: float | None = Field(None, gt=0, lt=500)