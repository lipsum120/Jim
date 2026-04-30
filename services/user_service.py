from repositories.user_repo import UserRepository


class UserService():
    def __init__(self, db):
        self.repo = UserRepository(db)
    
    def get_users(self):
        return self.repo.get_users()