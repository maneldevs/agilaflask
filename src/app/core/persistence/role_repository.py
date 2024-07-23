from src.app.core.application.domain import Role


class RoleRepository:

    def fetch_all(self):
        return [Role("1", "admin"), Role("2", "user")]

    def fetch_one_by_id(self, id: str):
        if (id != 1):
            return None
        return [Role("1", "admin")]
