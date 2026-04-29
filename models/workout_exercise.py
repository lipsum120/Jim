from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from core.database import Base


class WorkoutExercise(Base):
    
    __tablename__= "WorkoutExercise"
    
    id = Column(Integer, primary_key=True, index=True)
    target_reps = Column(Integer, nullable=False)
    target_sets = Column(Integer, nullable=False)
    target_duration = Column(Integer, nullable=False)
    
    workout_id = Column(Integer, ForeignKey("Workout.id"))
    exercise_id = Column(Integer, ForeignKey("Exercise.id"))
    
    workout = relationship("Workout", back_populates="workout_exercises")
    exercise = relationship("Exercise", back_populates="exercise_workouts")