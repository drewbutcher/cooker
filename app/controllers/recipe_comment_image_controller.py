from flask import render_template
from app.models import Comment

class RecipeCommentImageController:
    def index(self, recipe_id: int, comment_id: int) -> str:

        comment = Comment.query.filter(
            Comment.recipe_id == recipe_id,
            Comment.id == comment_id).first_or_404()

        recipe = comment.recipe
        images = comment.images

        return render_template(
            'recipes/comments/images/index.html',
            recipe=recipe,
            comment=comment,
            images=images)
