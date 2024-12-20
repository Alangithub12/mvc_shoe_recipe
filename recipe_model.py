class Recipe:
    def __init__(self, title, author, recipe_type, description, ingredients, cuisine, link=None):
        self.title = title
        self.author = author
        self.recipe_type = recipe_type  # 'первое', 'второе' и т.д.
        self.description = description
        self.ingredients = ingredients  # список ингредиентов
        self.cuisine = cuisine  # 'итальянская', 'французская', 'украинская' и т.д.
        self.link = link  # ссылка на рецепт

    def __str__(self):
        return f"{self.title} by {self.author} ({self.cuisine}) - {self.recipe_type}\n{self.description}\nИнгредиенты: {', '.join(self.ingredients)}\nСсылка: {self.link if self.link else 'Нет ссылки'}"