from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from models.exercise_muscle import ExerciseMuscle

class Muscle(Base):
    
    __tablename__ = "Muscle"
    
    muscle_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    
    exercises = relationship(
        "Exercise", 
        secondary=ExerciseMuscle,
        back_populates="muscles"    
    )