from app.controllers import RecipeCommentController
from app.routes.recipes.comments import bp

@bp.route('/recipes/<int:recipe_id>/comments', methods=['GET'])
def index(recipe_id: int):
    return RecipeCommentController().index(recipe_id)

@bp.route('/recipes/<int:recipe_id>/comments/<int:comment_id>', methods=['GET'])
def show(recipe_id: int, comment_id: int):
    return RecipeCommentController().show(recipe_id, comment_id)
