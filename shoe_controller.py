from shoe_model import Shoe
class ShoeController:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        self.shoes.append(shoe)

    def remove_shoe(self, shoe):
        self.shoes.remove(shoe)

    def get_all_shoes(self):
        return self.shoes

    def find_shoe_by_type(self, shoe_type):
        return [shoe for shoe in self.shoes if shoe.shoe_type == shoe_type]