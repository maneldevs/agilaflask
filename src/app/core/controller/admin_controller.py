from flask import Blueprint, render_template

bp: Blueprint = Blueprint("core_admin", __name__)


@bp.get("/core/admin")
def admin_index():
    return render_template("index.html")
