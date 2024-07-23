from src.app.core.application.domain import Role
from src.app.core.persistence.role_repository import RoleRepository
from src.app.shared.exceptions import EntityNotFoundError


class RoleService:

    def __init__(self, role_repository: RoleRepository) -> None:
        self.role_repository = role_repository

    def read_all(self) -> list[Role]:
        return self.role_repository.fetch_all()

    def read_one_by_id(self, id: str):
        role = self.role_repository.fetch_one_by_id(id)
        if role is None:
            raise EntityNotFoundError("Role not found")
        return role
