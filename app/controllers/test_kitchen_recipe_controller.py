from flask import render_template, redirect, request, url_for
from flask.typing import ResponseReturnValue

from app.models import Recipe, User

class TestKitchenRecipeController:

    def index(self) -> str:
        recipes = Recipe.query.all()
        return render_template('test_kitchen/recipes/index.html', recipes=recipes)

    def show(self, recipe_id: int) -> str:
        recipe = Recipe.query.get_or_404(recipe_id)
        return render_template('test_kitchen/recipes/show.html', recipe=recipe)

    def create(self) -> str:
        users = User.query.filter(User.is_author == True).all()
        return render_template('test_kitchen/recipes/create.html', users=users)

    def store(self) -> ResponseReturnValue:
        user = User.query.get_or_404(request.form.get("author_id", type=int))
        recipe = Recipe(
            title=request.form.get("title"),
            author=user)
        recipe.store_in_database()
        return redirect(url_for('test_kitchen.recipes.index'))

    def edit(self, recipe_id: int) -> str:
        recipe = Recipe.query.get_or_404(recipe_id)
        users = User.query.filter(User.is_author == True).all()
        return render_template(
            'test_kitchen/recipes/edit.html',
            recipe=recipe,
            users=users)

    def update(self, recipe_id: int) -> ResponseReturnValue:
        recipe = Recipe.query.get_or_404(recipe_id)
        author = User.query.get_or_404(request.form.get("author_id", type=int))

        recipe.title = request.form.get("title")
        recipe.author = author

        recipe.store_in_database()
        return redirect(url_for('test_kitchen.recipes.index'))

    def destroy(self, recipe_id: int) -> ResponseReturnValue:
        recipe = Recipe.query.get_or_404(recipe_id)
        recipe.delete_from_database()
        return redirect(url_for('test_kitchen.recipes.index'))