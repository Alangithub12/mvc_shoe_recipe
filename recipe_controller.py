from recipe_model import Recipe
class RecipeController:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def get_all_recipes(self):
        return self.recipes

    def find_recipe