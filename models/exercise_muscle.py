from sqlalchemy import Column, ForeignKey, Integer, Table

from core.database import Base

ExerciseMuscle = Table(
    "ExerciseMuscle",
    Base.metadata,
    Column("exercise_id", Integer, ForeignKey("Exercise.id"), primary_key=True),
    Column("muscle_id", Integer, ForeignKey("Muscle.id"), primary_key=True)
)