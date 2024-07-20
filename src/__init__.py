from flask import Flask
from flask_injector import FlaskInjector, singleton

from src.app.core.application.role_service import RoleService
from src.app.core.controller import role_controller


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/health")
    def health():
        return {"status": "UP"}

    app.register_blueprint(role_controller.bp)

    def configure(binder):
        binder.bind(RoleService, to=RoleService(), scope=singleton)

    FlaskInjector(app=app, modules=[configure])

    return app
