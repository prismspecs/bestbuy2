from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if percent < 0 or percent > 100:
            raise ValueError("percent must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        discount = self.percent / 100
        return product.price * quantity * (1 - discount)


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product: Product, quantity: int) -> float:
        pairs = quantity // 2
        remainder = quantity % 2
        return (pairs * 1.5 + remainder) * product.price


class ThirdOneFree(Promotion):
    def apply_promotion(self, product: Product, quantity: int) -> float:
        groups_of_three = quantity // 3
        remainder = quantity % 3
        return (groups_of_three * 2 + remainder) * product.price
