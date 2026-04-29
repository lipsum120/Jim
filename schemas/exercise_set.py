from pydantic import BaseModel


class ExerciseSet(BaseModel):
    id: int
    set_number: int
    duration: int
    rep: int
    
    class Config:
        orm_model = True