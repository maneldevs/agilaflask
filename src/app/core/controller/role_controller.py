from flask.views import MethodView
from flask_smorest import Blueprint
from injector import inject

from src.app.core.application.role_service import RoleService

bp: Blueprint = Blueprint("core_roles", __name__, description="Roles")


@bp.route("/api/core/roles")
class RoleList(MethodView):
    @inject
    def __init__(self, role_service: RoleService) -> None:
        self.role_service = role_service

    def get(self):
        return self.role_service.read_all() # TODO mmr to json


@bp.route("/api/core/roles/<string:id>")
class Role(MethodView):

    @inject
    def __init__(self, role_service: RoleService) -> None:
        self.role_service = role_service

    def get(self, id):
        return self.role_service.read_one_by_id(id)
