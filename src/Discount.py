class Discount:
    def __init__(self, discounted_price, required_quantity) -> None:
        self.required_quantity = required_quantity
        self.discounted_price = discounted_price

    def get_required_quantity(self) -> int:
        return self.required_quantity

    def get_discounted_price(self) -> int:
        return self.discounted_price

    def __str__(self) -> str:
        return "Discount(%d, %d)" % (self.discounted_price, self.required_quantity)

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.discounted_price == other.discounted_price and self.required_quantity == other.required_quantity

    def __hash__(self) -> int:
        return hash((self.discounted_price, self.required_quantity))
