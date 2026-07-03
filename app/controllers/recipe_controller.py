from flask import render_template

from app.models import Recipe

class RecipeController:
    def index(self) -> str:
        recipes = Recipe.query.all()
        return render_template('recipes/index.html', recipes=recipes)

    def show(self, recipe_id: int) -> str:
        recipe = Recipe.query.get_or_404(recipe_id)
        return render_template('recipes/show.html', recipe=recipe)