from flask import Blueprint

bp = Blueprint('recipes', __name__)

from app.routes.recipes import routes

from app.routes.recipes.comments import bp as recipes_comments_blueprint
bp.register_blueprint(recipes_comments_blueprint)
