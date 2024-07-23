import pytest

from src.app.core.application.domain import Role


@pytest.fixture
def role_admin():
    return Role(id="123abc", code="admin")


@pytest.fixture
def role_user():
    return Role(id="456def", code="user")


@pytest.fixture
def role_list(role_admin, role_user):
    return [role_admin, role_user]
