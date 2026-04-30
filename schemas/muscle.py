from typing import List
from pydantic import BaseModel


class Muscle(BaseModel):
    id: int
    name: str
    # exercises: List["Exercise"] = []
    
    # class Config:
    #     orm_mode = True
        