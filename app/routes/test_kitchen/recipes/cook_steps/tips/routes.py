from app.controllers import TestKitchenRecipeCookStepTipController
from app.routes.test_kitchen.recipes.cook_steps.tips import bp

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>/tips', methods=['GET'])
def index(recipe_id: int, cook_step_id: int):
    return TestKitchenRecipeCookStepTipController().index(recipe_id, cook_step_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>/tips/<int:tip_id>', methods=['GET'])
def show(recipe_id: int, cook_step_id: int, tip_id: int):
    return TestKitchenRecipeCookStepTipController().show(recipe_id, cook_step_id, tip_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>/tips/create', methods=['GET'])
def create(recipe_id: int, cook_step_id: int):
    return TestKitchenRecipeCookStepTipController().create(recipe_id, cook_step_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>/tips', methods=['POST'])
def store(recipe_id: int, cook_step_id: int):
    return TestKitchenRecipeCookStepTipController().store(recipe_id, cook_step_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>/tips/<int:tip_id>/edit', methods=['GET'])
def edit(recipe_id: int, cook_step_id: int, tip_id: int):
    return TestKitchenRecipeCookStepTipController().edit(recipe_id, cook_step_id, tip_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>/tips/<int:tip_id>', methods=['POST'])
def update(recipe_id: int, cook_step_id: int, tip_id: int):
    return TestKitchenRecipeCookStepTipController().update(recipe_id, cook_step_id, tip_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>/tips/<int:tip_id>/delete', methods=['POST'])
def destroy(recipe_id: int, cook_step_id: int, tip_id: int):
    return TestKitchenRecipeCookStepTipController().destroy(recipe_id, cook_step_id, tip_id)
