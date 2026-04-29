from pydantic import BaseModel
from schemas.exercise import Exercise


class WorkoutExercise(BaseModel):
    id: int
    target_reps: int
    target_sets: int
    target_duration: int
    exercise: Exercise
    
    class Config:
        orm_model = True