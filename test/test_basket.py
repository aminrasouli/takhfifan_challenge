import pytest

from main import define_base_product
from src.Basket import Basket


@pytest.fixture()
def resource():
    basket = Basket()
    products = define_base_product()
    return basket, products


class TestBasket:
    def test_one(self, resource) -> None:
        basket, products = resource
        basket.add(products["A"])
        basket.add(products["B"])
        basket.add(products["C"])
        basket.add(products["D"])
        assert basket.total == 75000

    def test_two(self, resource) -> None:
        basket, products = resource
        basket.add(products["A"])
        basket.add(products["B"])
        basket.add(products["D"])
        assert basket.total == 65000

    def test_three(self, resource) -> None:
        basket, products = resource
        basket.add(products["A"])
        basket.add(products["B"], 2)
        basket.add(products["C"])
        basket.add(products["D"])
        assert basket.total == 90000

    def test_four(self, resource) -> None:
        basket, products = resource
        basket.add(products["A"], 4)
        basket.add(products["B"], 5)
        basket.add(products["C"])
        basket.add(products["D"])
        assert basket.total == 215000

    def test_five(self, resource) -> None:
        basket, products = resource
        basket.add(products["A"], 2)
        basket.add(products["B"])
        basket.add(products["C"])
        basket.add(products["D"], 3)
        assert basket.total == 125000

    def test_six(self, resource) -> None:
        basket, products = resource
        basket.add(products["A"])
        basket.add(products["B"])
        basket.add(products["C"], 4)
        basket.add(products["D"])
        assert basket.total == 105000

    def test_seven(self, resource) -> None:
        basket, products = resource
        basket.add(products["A"], 4)
        basket.add(products["B"])
        basket.add(products["C"])
        basket.add(products["D"])
        assert basket.total == 125000
