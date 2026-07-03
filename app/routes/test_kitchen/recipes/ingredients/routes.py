from app.controllers import TestKitchenRecipeIngredientController
from app.routes.test_kitchen.recipes.ingredients import bp

@bp.route('/test-kitchen/recipes/<int:recipe_id>/ingredients', methods=['GET'])
def index(recipe_id: int):
    return TestKitchenRecipeIngredientController().index(recipe_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>', methods=['GET'])
def show(recipe_id: int, ingredient_id: int):
    return TestKitchenRecipeIngredientController().show(recipe_id, ingredient_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/ingredients/create', methods=['GET'])
def create(recipe_id: int):
    return TestKitchenRecipeIngredientController().create(recipe_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/ingredients', methods=['POST'])
def store(recipe_id: int):
    return TestKitchenRecipeIngredientController().store(recipe_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>/edit', methods=['GET'])
def edit(recipe_id: int, ingredient_id: int):
    return TestKitchenRecipeIngredientController().edit(recipe_id, ingredient_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>', methods=['POST'])
def update(recipe_id: int, ingredient_id: int):
    return TestKitchenRecipeIngredientController().update(recipe_id, ingredient_id)

@bp.route('/test-kitchen/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>/delete', methods=['POST'])
def destroy(recipe_id: int, ingredient_id: int):
    return TestKitchenRecipeIngredientController().destroy(recipe_id, ingredient_id)
