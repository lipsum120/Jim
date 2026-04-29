from typing import List

from pydantic import BaseModel

from schemas.workout_exercise import WorkoutExercise


class Workout(BaseModel):
    id: int
    name: str
    exercises: List[WorkoutExercise] = []
    
    class Config:
        orm_mode: bool = True