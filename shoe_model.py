class Shoe:
    def __init__(self, shoe_type, shoe_kind, color, price, manufacturer, size):
        self.shoe_type = shoe_type  # 'мужская' или 'женская'
        self.shoe_kind = shoe_kind  # 'кроссовки', 'сапоги', 'сандалии', 'туфли' и т.д.
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        return f"{self.shoe_type} {self.shoe_kind} - {self.color}, {self.size} - {self.price} руб. ({self.manufacturer})"