from unittest import TestCase
from unittest.mock import patch

import pytest

from src.app.core.application.domain import Role
from src.app.core.application.role_service import RoleService


@patch("src.app.core.application.role_service.RoleRepository")
class RoleServiceTest(TestCase):

    @pytest.fixture(autouse=True)
    def prepare_fixture(self, role_list: list[Role]):
        self.role_list = role_list

    def test_role_service_read_all_return_list(self, mock_repo):
        repo = mock_repo.return_value
        repo.fetch_all.return_value = self.role_list
        service_under_test: RoleService = RoleService(repo)
        result: list[Role] = service_under_test.read_all()
        self.assertEqual(2, len(result))
        self.assertTrue(result.__contains__(self.role_list[0]))
        self.assertTrue(result.__contains__(self.role_list[1]))
