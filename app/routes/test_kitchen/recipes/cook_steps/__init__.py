from flask import Blueprint

bp = Blueprint('cook_steps', __name__)

from app.routes.test_kitchen.recipes.cook_steps import routes

from app.routes.test_kitchen.recipes.cook_steps.tips import bp as test_kitchen_recipes_cook_steps_tips_blueprint
bp.register_blueprint(test_kitchen_recipes_cook_steps_tips_blueprint)
