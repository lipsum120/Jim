from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from core.database import Base


class WorkoutExercise(Base):
    
    __tablename__= "WorkoutExercise"
    
    workout_exercise_id = Column(Integer, primary_key=True, index=True)
    target_reps = Column(Integer, nullable=False)
    workout_id = Column(Integer, ForeignKey("Workout.workout_id"))
    exercise_id = Column(Integer, ForeignKey("Exercise.exercise_id"))
    
    workout = relationship("Workout", back_populates="workout_exercises")
    exercise = relationship("Exercise", back_populates="exercise_workouts")
    exercise_sets = relationship("ExerciseSet", back_populates="workout_exercise")