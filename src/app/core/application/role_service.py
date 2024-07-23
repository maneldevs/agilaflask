from src.app.core.application.domain import Role
from src.app.core.persistence.role_repository import RoleRepository


class RoleService:

    def __init__(self, role_repository: RoleRepository) -> None:
        self.role_repository = role_repository

    def read_all(self) -> list[Role]:
        return self.role_repository.fetch_all()
