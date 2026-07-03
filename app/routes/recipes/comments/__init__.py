from flask import Blueprint

bp = Blueprint('comments', __name__)

from app.routes.recipes.comments import routes

from app.routes.recipes.comments.images import bp as recipes_comments_images_blueprint
bp.register_blueprint(recipes_comments_images_blueprint)
