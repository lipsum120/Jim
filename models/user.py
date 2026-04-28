from sqlalchemy import Column, Float, Integer, String
from core.database import Base


class User(Base):
    
    __tablename__ = "User"
    
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    height = Column(Float(5,2))
    # weight = Column(Float(5, 2))