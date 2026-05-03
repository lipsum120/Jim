from typing import List

from pydantic import BaseModel

from schemas.workout_exercise import WorkoutExercise


class Workout(BaseModel):
    id: int
    name: str
    exercises: List[WorkoutExercise] = []
    
    model_config = {"from_attributes": True}