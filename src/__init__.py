from flask import Flask
from flask_injector import FlaskInjector, singleton

from src.app.core.application.role_service import RoleService
from src.app.core.controller import role_controller
from src.app.core.persistence.role_repository import RoleRepository


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/health")
    def health():
        return {"status": "UP"}

    app.register_blueprint(role_controller.bp)

    def configure(binder):
        binder.bind(RoleRepository, to=RoleRepository(), scope=singleton)
        binder.bind(RoleService, to=RoleService(RoleRepository()), scope=singleton)

    FlaskInjector(app=app, modules=[configure])

    return app
