from repositories.muslce_repo import MuscleRepository


class MuscleService():
    def __init__(self, repo: MuscleRepository):
        self.repo = repo
    