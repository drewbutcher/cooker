from app.controllers import TestKitchenRecipeController
from app.routes.test_kitchen.recipes import bp

@bp.route('/test-kitchen/recipes', methods=['GET'])
def index():
    return TestKitchenRecipeController().index()

@bp.route('/test-kitchen/recipes/<int:recipe_id>', methods=['GET'])
def show(recipe_id: int):
    return TestKitchenRecipeController().show(recipe_id)

@bp.route('/test-kitchen/recipes/create', methods=['GET'])
def create():
    return TestKitchenRecipeController().create()

@bp.route('/test-kitchen/recipes', methods=['POST'])
def store():
    return TestKitchenRecipeController().store()

@bp.route('/test-kitchen/recipes/<int:recipe_id>/edit', methods=['GET'])
def edit(recipe_id: int):
    return TestKitchenRecipeController().edit(recipe_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>', methods=['POST'])
def update(recipe_id: int):
    return TestKitchenRecipeController().update(recipe_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/delete', methods=['POST'])
def destroy(recipe_id: int):
    return TestKitchenRecipeController().destroy(recipe_id)
