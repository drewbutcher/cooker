from app.controllers import RecipeCommentImageController
from app.routes.recipes.comments.images import bp

@bp.route('/recipes/<int:recipe_id>/comments/<int:comment_id>/images', methods=['GET'])
def index(recipe_id: int, comment_id: int):
    return RecipeCommentImageController().index(recipe_id, comment_id)
