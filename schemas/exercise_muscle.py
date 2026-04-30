from pydantic import BaseModel
from schemas.exercise import Exercise


class ExerciseMuscle(BaseModel):
    muscle: Muscle
    
    class Config:
        orm_model = True