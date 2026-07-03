from flask import Blueprint

bp = Blueprint('images', __name__)

from app.routes.recipes.comments.images import routes
