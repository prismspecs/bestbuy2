from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    # abstract class for promotions

    def __init__(self, name: str):
        # initializes the promotion with a name
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        # abstract method to apply the promotion
        pass


class PercentDiscount(Promotion):
    # percentage discount promotion

    def __init__(self, name: str, percent: float):
        # initializes the promotion with a name and discount percentage
        super().__init__(name)
        if percent < 0 or percent > 100:
            raise ValueError("percent must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        # applies the percentage discount to the total price
        discount = self.percent / 100
        return product.price * quantity * (1 - discount)


class SecondHalfPrice(Promotion):
    # second item at half price promotion

    def apply_promotion(self, product: Product, quantity: int) -> float:
        # calculates the total price with the promotion applied
        pairs = quantity // 2
        remainder = quantity % 2
        return (pairs * 1.5 + remainder) * product.price


class ThirdOneFree(Promotion):
    # buy 2, get 1 free promotion

    def apply_promotion(self, product: Product, quantity: int) -> float:
        # calculates the total price with the promotion applied
        groups_of_three = quantity // 3
        remainder = quantity % 3
        return (groups_of_three * 2 + remainder) * product.price
