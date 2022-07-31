import sys
from typing import Dict, List

import pytest

from src.Discount import Discount
from src.Product import Product


class ProductFactory:
    @staticmethod
    def create_product(name: object, price: int, discounts: List[Discount] = None) -> Product:
        product = Product(name, price)
        if discounts is not None:
            product.add_discount(discounts)
        return product


def define_base_product() -> Dict[str, Product]:
    return {
        "A": ProductFactory.create_product("A", 20000, [Discount(50000, 3)]),
        "B": ProductFactory.create_product("B", 30000, [Discount(45000, 2)]),
        "C": ProductFactory.create_product("C", 10000),
        "D": ProductFactory.create_product("D", 15000),
    }


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", "-s", "test/test_basket.py"]))
