from flask import Flask, jsonify
from flask_injector import FlaskInjector, singleton
from flask_smorest import Api

from src.app.core.application.role_service import RoleService
from src.app.core.controller import admin_controller, role_controller
from src.app.core.persistence.role_repository import RoleRepository
from src.app.shared.exceptions import BaseError


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(admin_controller.bp)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Agila"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/api/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    api.register_blueprint(role_controller.bp)

    @app.errorhandler(BaseError)
    def base_handler(exc: BaseError):
        return jsonify(message=exc.message, status=exc.status_code), exc.status_code

    def configure(binder):
        binder.bind(RoleRepository, to=RoleRepository(), scope=singleton)
        binder.bind(RoleService, to=RoleService(RoleRepository()), scope=singleton)

    FlaskInjector(app=app, modules=[configure])

    @app.route("/health")
    def health():
        return {"status": "UP"}

    return app
