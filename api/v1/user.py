from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.user import User
from services.user_service import UserService

router = APIRouter (
    prefix = "/users", tags = ["users"] 
)

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_users()