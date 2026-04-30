from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.enums import ExerciseType
from models.exercise_muscle import ExerciseMuscle

class Exercise(Base):
    
    __tablename__ = "Exercise"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    instruction = Column(String(510), nullable=False)
    exercise_types = Column(Enum(ExerciseType))
    
    muscles = relationship(
        "Muscle", 
        secondary=ExerciseMuscle,
        back_populates="exercises"    
    )
    
    exercise_workouts = relationship(
        "WorkoutExercise",
        back_populates="exercise"
    )