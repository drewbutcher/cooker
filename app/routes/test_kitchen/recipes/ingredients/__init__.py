from flask import Blueprint

bp = Blueprint('ingredients', __name__)

from app.routes.test_kitchen.recipes.ingredients import routes
