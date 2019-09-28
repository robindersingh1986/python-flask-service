#-----blueprints/simple_templates.py-----
from flask import Blueprint

user = Blueprint('user', __name__)


@user.route("/")
def user_home():
    return "Hello, User!"

@user.route("/user-detail")
def user_detail():
    return {
      'name': 'rob',
      'age': 33
    }
