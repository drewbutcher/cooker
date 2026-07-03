from flask import Blueprint

bp = Blueprint('tips', __name__)

from app.routes.test_kitchen.recipes.cook_steps.tips import routes
