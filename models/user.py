from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base


class User(Base):
    
    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    height = Column(Float(5,2), nullable=False)
    weight = Column(Float(5, 2), nullable=False)
    
    workouts = relationship("Workout", back_populates="user")