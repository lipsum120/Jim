from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base


class Workout(Base):
    
    __tablename__ = "Workout"
    
    workout_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)
    
    user = relationship("User", back_populates="workouts")
    
    workout_exercises = relationship(
        "WorkoutExercise",
        back_populates="workout"
    )