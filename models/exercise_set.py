import enum
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base

class ExerciseSet(Base):
    
    __tablename__ = "ExerciseSet"
    
    exercise_set_id = Column(Integer, primary_key=True, index=True)
    set_number = Column(Integer)
    duration = Column(Integer)
    reps = Column(Integer)
    workout_exercise_id = Column(Integer, ForeignKey("WorkoutExercise.workout_exercise_id"))
    
    workout_exercise = relationship(
        "WorkoutExercise", 
        back_populates="exercise_sets"    
    )