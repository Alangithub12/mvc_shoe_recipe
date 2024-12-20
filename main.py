from shoe_model import Shoe
from shoe_controller import ShoeController
from shoe_view import ShoeView

if __name__ == "__main__":
    controller = ShoeController()
    view = ShoeView()

    # Добавление обуви
    shoe1 = Shoe("мужская", "кроссовки", "черный", 5000, "Nike", 42)
    shoe2 = Shoe("женская", "туфли", "красный", 3000, "Adidas", 38)

    controller.add_shoe(shoe1)
    controller.add_shoe(shoe2)

    # Отображение всех обуви
    view.display_message("Список обуви:")
    view.display_shoes(controller.get_all_shoes())

    # Поиск обуви по типу
    view.display_message("Поиск мужской обуви:")
    male_shoes = controller.find_shoe_by_type("мужская")
    view.display_shoes(male_shoes)