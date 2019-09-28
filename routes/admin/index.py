#-----blueprints/simple_templates.py-----
from flask import Blueprint

admin = Blueprint('admin', __name__)


@admin.route("/")
def home():
    return "Welcome to admin !"

@admin.route("/test")
def test():
    return "<h1>This is test route</h1>"
    