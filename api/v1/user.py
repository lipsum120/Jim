from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.v1.deps import get_user_service
from core.database import get_db
from schemas.user import User
from services.user_service import UserService

router = APIRouter (
    prefix = "/users", tags = ["users"] 
)

@router.get("/")
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()