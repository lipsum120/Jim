from sqlalchemy import Column, ForeignKey, Integer, Table

from core.database import Base

ExerciseMuscle = Table(
    "ExerciseMuscle",
    Base.metadata,
    Column("exercise_id", Integer, ForeignKey("Exercise.exercise_id"), primary_key=True),
    Column("muscle_id", Integer, ForeignKey("Muscle.muscle_id"), primary_key=True)
)