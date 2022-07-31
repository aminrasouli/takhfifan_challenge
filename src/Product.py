from typing import List

from src.Discount import Discount


class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.discounts = []

    def get_price(self) -> int:
        return self.price

    def add_discount(self, discounts: List[Discount]) -> None:
        if not isinstance(discounts, list):
            discounts = [discounts]
        self.discounts.extend(discounts)

    def get_discounts(self) -> List[Discount]:
        return self.discounts

    def has_discount(self) -> bool:
        return len(self.discounts) > 0

    def __hash__(self) -> int:
        return hash(f"{self.name}-{self.price}")

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.price == other.price

    def __str__(self) -> str:
        return f"{self.name} - {self.price}"

    def __repr__(self) -> str:
        return self.__str__()
