from flask import Blueprint

bp = Blueprint('test_kitchen', __name__)

from app.routes.test_kitchen import routes

from app.routes.test_kitchen.recipes import bp as test_kitchen_recipes_blueprint
bp.register_blueprint(test_kitchen_recipes_blueprint)
