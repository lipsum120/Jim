from fastapi import HTTPException, status
from models.user import User
from repositories.user_repo import UserRepository
from schemas.user import UserCreate, UserUpdate
from services.utils import get_or_404



class UserService():
    def __init__(self, repo: UserRepository):
        self.repo = repo
    
    def _get_user(self, user_id: int) -> User:
         return get_or_404(self.repo.get_user_by_id(user_id), "User")
    
    def get_users(self) -> list[User]:
        return self.repo.get_users()
    
    
    def get_user(self, user_id: int) -> User:
        return self._get_user(user_id)
    
    
    def create_user(self, data: UserCreate) -> User:
        return self.repo.create_user(data)
    
    
    def update_user(self, user_id: int, data: UserUpdate) -> User:
        user = self._get_user(user_id)
        return self.repo.update_user(user, data)
    
    
    def delete_user(self, user_id: int) -> None:
        user = self._get_user(user_id)
        self.repo.delete_user(user)