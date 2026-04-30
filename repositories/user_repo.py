from models.user import User


class UserRepository():
    def __init__(self, db):
        self.db = db
    
    def get_users(self):
        return self.db.query(User).all()