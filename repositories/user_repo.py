from models.user import User
from schemas.user import UserCreate, UserUpdate


class UserRepository():
    def __init__(self, db):
        self.db = db
    
    def get_users(self) -> list[User]:
        return self.db.query(User).all()
    
    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.get(User, user_id)
    
    def create_user(self, data: UserCreate) -> User:
        user = User(**data.model_dump())
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        
        return user

    def update_user(self, user: User, data: UserUpdate) -> User:
        update_data = data.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(user, key, value)
            
        self.db.commit()
        self.db.refresh(user)
            
        return user
    
    def delete_user(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()