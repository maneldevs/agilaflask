# Aplicació en Flask

# 1. Instal·lació

- Crear el entorn de desenvolupament en VSCODE en DEV CONTAINERS
- Obrir el contenidor en el directori del projecte
- Crear el entorn virtual, activar-lo i verificar el seu funcionament:
```bash
python3 -m venv .venv
source .venv/bin/activate
which python
```
Nota: Per desactivarlo: deactivate
- Instal·lar flask i dependencies
```bash
pip install flask
pip install python-dotenv
pip install flask-smorest
pip install Flask-Injector
pip freeze > requirements.txt
```

# 2. Configuració

- Crear .gitignore
- Crear .env
- Crear la estructura de directoris
- Crear el fitxer __init__.py dins de src
- Probar la aplicació:
```bash
flask --app src run --debug
```
Nota: Escrivint en .env lo següent podem executar l'aplicació amb només -> flask run --debug:
```
FLASK_DEBUG=True
FLASK_APP=src
```

# 3. Injecció de dependències
- En el fitxer d'entrada (__init__.y) afegir la configuració de les dependències:
```py
from flask_injector import FlaskInjector, singleton
def configure(binder):
        binder.bind(RoleRepository, to=RoleRepository(), scope=singleton)
        binder.bind(RoleService, to=RoleService(RoleRepository()), scope=singleton)

FlaskInjector(app=app, modules=[configure])
```
- Per injectar una dependència anotar amb @inject:
```py
@bp.get("/api/core/roles")
@inject
def get_all_roles(role_service: RoleService):
    return role_service.read_all()
```

# 4. Smorest: Blueprints i OpenApi
- Crear un fitxer en controllers i definir el blueprint
```py
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
        return self.role_service.read_all()
```

- Configurar i asignar els blueprints
```py
from flask_smorest import Api
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Agila"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/api/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(role_controller.bp)
```

- Per vore la documentació de swagger obrir el navegador i anar a http://localhost:5000/api/docs

# 5. Tests

- Instal·lar pytest

```bash
pip install pytest
```