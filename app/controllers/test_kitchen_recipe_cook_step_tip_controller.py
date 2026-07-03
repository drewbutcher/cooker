from flask import render_template, redirect, url_for
from flask.typing import ResponseReturnValue

from app.models import CookStep, Tip, Recipe

class TestKitchenRecipeCookStepTipController:

    def index(self, recipe_id: int, cook_step_id: int) -> str:
        cook_step = CookStep.query.filter(
            CookStep.id == cook_step_id,
            CookStep.recipe_id == recipe_id
        ).first_or_404()
        tips = cook_step.tips
        recipe = cook_step.recipe
        return render_template(
            'test_kitchen/recipes/cook_steps/tips/index.html',
            recipe=recipe,
            cook_step=cook_step,
            tips=tips)

    def show(self, recipe_id: int, cook_step_id: int, tip_id: int) -> str:
        # recipe to own the cook_step
        cook_step = CookStep.query.filter(
            CookStep.id == cook_step_id,
            CookStep.recipe_id == recipe_id
        ).first_or_404()
        # cook_step to own the tip
        tip = Tip.query.filter(
            Tip.id == tip_id,
            Tip.cook_step_id == cook_step_id
        ).first_or_404()
        recipe = cook_step.recipe

        return render_template(
            'test_kitchen/recipes/cook_steps/tips/show.html',
            recipe=recipe,
            cook_step=cook_step,
            tip=tip)

    def create(self, recipe_id: int, cook_step_id: int) -> str:
        return render_template('test_kitchen/recipes/cook_steps/tips/create.html')

    def store(self, recipe_id: int, cook_step_id: int) -> ResponseReturnValue:
        return redirect(url_for('test_kitchen.recipes.cook_steps.tips.index', recipe_id=recipe_id, cook_step_id=cook_step_id))

    def edit(self, recipe_id: int, cook_step_id: int, tip_id: int) -> str:
        return render_template('test_kitchen/recipes/cook_steps/tips/edit.html')

    def update(self, recipe_id: int, cook_step_id: int, tip_id: int) -> ResponseReturnValue:
        return redirect(url_for('test_kitchen.recipes.cook_steps.tips.index', recipe_id=recipe_id, cook_step_id=cook_step_id))

    def destroy(self, recipe_id: int, cook_step_id: int, tip_id: int) -> ResponseReturnValue:
        return redirect(url_for('test_kitchen.recipes.cook_steps.tips.index', recipe_id=recipe_id, cook_step_id=cook_step_id))