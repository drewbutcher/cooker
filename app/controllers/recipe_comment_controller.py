from flask import render_template

from app.models import Comment, Recipe

class RecipeCommentController:
    def index(self, recipe_id: int) -> str:
        recipe = Recipe.query.get_or_404(recipe_id)
        comments = recipe.comments
        return render_template(
            'recipes/comments/index.html',
            recipe=recipe,
            comments=comments)

    def show(self, recipe_id: int, comment_id: int) -> str:
        comment = Comment.query.filter(
            Comment.id == comment_id,
            Comment.recipe_id == recipe_id).first_or_404()

        recipe = comment.recipe

        return render_template(
            'recipes/comments/show.html',
            comment=comment,
            recipe=recipe)