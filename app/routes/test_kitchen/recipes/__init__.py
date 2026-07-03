from flask import Blueprint

bp = Blueprint('recipes', __name__)

from app.routes.test_kitchen.recipes import routes

from app.routes.test_kitchen.recipes.cook_steps import bp as test_kitchen_recipes_cook_steps_blueprint
bp.register_blueprint(test_kitchen_recipes_cook_steps_blueprint)

from app.routes.test_kitchen.recipes.ingredients import bp as test_kitchen_recipes_ingredients_blueprint
bp.register_blueprint(test_kitchen_recipes_ingredients_blueprint)
