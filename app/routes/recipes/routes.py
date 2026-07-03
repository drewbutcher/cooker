from app.controllers import RecipeController
from app.routes.recipes import bp

@bp.route('/recipes', methods=['GET'])
def index():
    return RecipeController().index()

@bp.route('/recipes/<int:recipe_id>', methods=['GET'])
def show(recipe_id: int):
    return RecipeController().show(recipe_id)
