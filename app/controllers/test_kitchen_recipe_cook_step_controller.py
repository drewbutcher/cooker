from flask import render_template, redirect, url_for
from flask.typing import ResponseReturnValue

from app.models import CookStep, Recipe

class TestKitchenRecipeCookStepController:

    def index(self, recipe_id: int) -> str:
        recipe = Recipe.query.get_or_404(recipe_id)
        return render_template('test_kitchen/recipes/cook_steps/index.html', recipe=recipe)

    def show(self, recipe_id: int, cook_step_id: int) -> str:
        cook_step = CookStep.query.filter(
            CookStep.id == cook_step_id,
            CookStep.recipe_id == recipe_id
        ).first_or_404()
        recipe = cook_step.recipe
        return render_template(
            'test_kitchen/recipes/cook_steps/show.html',
            recipe=recipe,
            cook_step=cook_step)

    def create(self, recipe_id: int) -> str:
        return render_template('test_kitchen/recipes/cook_steps/create.html')

    def store(self, recipe_id: int) -> ResponseReturnValue:
        return redirect(url_for('test_kitchen.recipes.cook_steps.index', recipe_id=recipe_id))

    def edit(self, recipe_id: int, cook_step_id: int) -> str:
        return render_template('test_kitchen/recipes/cook_steps/edit.html')

    def update(self, recipe_id: int, cook_step_id: int) -> ResponseReturnValue:
        return redirect(url_for('test_kitchen.recipes.cook_steps.index', recipe_id=recipe_id))

    def destroy(self, recipe_id: int, cook_step_id: int) -> ResponseReturnValue:
        return redirect(url_for('test_kitchen.recipes.cook_steps.index', recipe_id=recipe_id))