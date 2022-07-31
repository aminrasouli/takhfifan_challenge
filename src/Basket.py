from collections import defaultdict

from src.Discount import Discount
from src.Product import Product


class Basket:
    def __init__(self) -> None:
        self.items = defaultdict(int)
        self.__total = None

    def add(self, item: Product, quantity=1) -> None:
        self.items[item] += quantity

    def get_quantity(self, item: Product) -> int:
        return self.items[item]

    @staticmethod
    def calc_normal_item(price: int, quantity: int) -> int:
        return price * quantity

    def calc_discounted_item(self, item: Product, discount: Discount) -> int:
        discount_ratio = self.get_quantity(item) // discount.get_required_quantity()
        discounted_price_items = discount.get_discounted_price() * discount_ratio
        normal_price_items = (self.get_quantity(item) - (
                discount.get_required_quantity() * discount_ratio)) * item.get_price()
        return discounted_price_items + normal_price_items

    def calculate_total(self) -> int:
        total = 0
        for item in self.items:
            if item.has_discount():
                for discount in item.get_discounts():
                    if self.get_quantity(item) >= discount.required_quantity:
                        total += self.calc_discounted_item(item, discount)
                        break
                    else:
                        total += self.calc_normal_item(item.get_price(), self.get_quantity(item))
            else:
                total += self.calc_normal_item(item.get_price(), self.get_quantity(item))
        return total

    @property
    def total(self) -> int:
        if self.__total is None:
            self.__total = self.calculate_total()
        return self.__total

    def __str__(self) -> str:
        return str(self.items)

    def __repr__(self) -> str:
        return self.__str__()
