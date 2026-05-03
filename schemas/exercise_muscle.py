from pydantic import BaseModel


class ExerciseRef(BaseModel):
    id: int
    name: str
    
class MuscleRef(BaseModel):
    id: int
    name: str