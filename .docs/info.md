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
pip freeze > requirements.txt
```

# 2. Configuració
- Crear .gitignore
- Crear .env
- Crear la estructura de directoris