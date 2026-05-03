from pydantic import BaseModel


class ExerciseSet(BaseModel):
    id: int
    set_number: int
    duration: int
    rep: int
    
    model_config = {"from_attributes": True}