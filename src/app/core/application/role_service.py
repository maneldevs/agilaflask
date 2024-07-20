from src.app.core.persistence import role_repository


class RoleService:

    def __init__(self, role_repository: role_repository) -> None:
        self.role_repository = role_repository

    def read_all(self):
        return self.role_repository.fetch_all()
