from src.app.core.application.domain import Role


class RoleRepository:

    def fetch_all(self):
        return [Role("1", "admin"), Role("2", "user")]
