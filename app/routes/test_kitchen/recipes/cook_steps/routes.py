from app.controllers import TestKitchenRecipeCookStepController
from app.routes.test_kitchen.recipes.cook_steps import bp

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps', methods=['GET'])
def index(recipe_id: int):
    return TestKitchenRecipeCookStepController().index(recipe_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>', methods=['GET'])
def show(recipe_id: int, cook_step_id: int):
    return TestKitchenRecipeCookStepController().show(recipe_id, cook_step_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/create', methods=['GET'])
def create(recipe_id: int):
    return TestKitchenRecipeCookStepController().create(recipe_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps', methods=['POST'])
def store(recipe_id: int):
    return TestKitchenRecipeCookStepController().store(recipe_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>/edit', methods=['GET'])
def edit(recipe_id: int, cook_step_id: int):
    return TestKitchenRecipeCookStepController().edit(recipe_id, cook_step_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>', methods=['POST'])
def update(recipe_id: int, cook_step_id: int):
    return TestKitchenRecipeCookStepController().update(recipe_id, cook_step_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/cook-steps/<int:cook_step_id>/delete', methods=['POST'])
def destroy(recipe_id: int, cook_step_id: int):
    return TestKitchenRecipeCookStepController().destroy(recipe_id, cook_step_id)
