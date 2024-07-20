from flask import Blueprint
from injector import inject

from src.app.core.application.role_service import RoleService

bp: Blueprint = Blueprint("api_core_roles", __name__)


@bp.get("/api/core/roles")
@inject
def get_all_roles(role_service: RoleService):
    return role_service.read_all()
