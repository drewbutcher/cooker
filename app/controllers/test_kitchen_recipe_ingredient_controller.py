from flask import render_template, redirect, url_for
from flask.typing import ResponseReturnValue

class TestKitchenRecipeIngredientController:

    def index(self, recipe_id: int) -> str:
        return render_template('test_kitchen/recipes/ingredients/index.html')

    def show(self, recipe_id: int, ingredient_id: int) -> str:
        return render_template('test_kitchen/recipes/ingredients/show.html')

    def create(self, recipe_id: int) -> str:
        return render_template('test_kitchen/recipes/ingredients/create.html')

    def store(self, recipe_id: int) -> ResponseReturnValue:
        return redirect(url_for('test_kitchen.recipes.ingredients.index', recipe_id=recipe_id))

    def edit(self, recipe_id: int, ingredient_id: int) -> str:
        return render_template('test_kitchen/recipes/ingredients/edit.html')

    def update(self, recipe_id: int, ingredient_id: int) -> ResponseReturnValue:
        return redirect(url_for('test_kitchen.recipes.ingredients.index', recipe_id=recipe_id))

    def destroy(self, recipe_id: int, ingredient_id: int) -> ResponseReturnValue:
        return redirect(url_for('test_kitchen.recipes.ingredients.index', recipe_id=recipe_id))