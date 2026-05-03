from fastapi import Depends
from sqlmodel import Session
from core.database import get_db
from repositories.user_repo import UserRepository
from services.user_service import UserService


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repo = UserRepository(db)
    return UserService(repo)