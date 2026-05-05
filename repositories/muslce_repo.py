from models.muscle import Muscle


class MuscleRepository():
    def __init__(self, db):
        self.db = db
    
    def get_muscles(self) -> list[Muscle]:
        return self.db.query(Muscle).all()
    
    def get_muscle_by_id(self, id: int) -> Muscle:
        return self.db.query(Muscle).get(Muscle, id)

    def create_muscle(self, data) -> Muscle:
        muscle = Muscle(**data.model_dump())
        
        self.db.add(muscle)
        self.db.commit()
        self.db.refresh(muscle)
        
        return muscle
    
    def update_muscle(self, muscle: Muscle, data) -> Muscle:
        update_data = data.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(muscle, key, value)
        
        self.db.commit()
        self.db.refresh(muscle)
        
        return muscle
    
    def delete_user(self, muscle: Muscle) -> None:
        self.db.delete(muscle)
        self.db.commit