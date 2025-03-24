class Product:
    # represents a product in the store

    def __init__(self, name: str, price: float, quantity: int):
        # initializes the product with a name, price, and quantity
        if not name.strip():
            raise ValueError("name cannot be empty.")
        if price < 0:
            raise ValueError("price cannot be negative.")
        if quantity < 0:
            raise ValueError("quantity cannot be negative.")

        self._name = name
        self._price = price
        self._quantity = quantity
        self.active = True
        self.promotion = None  # promotion applied to the product

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative.")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("quantity cannot be negative.")
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self._quantity

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("not enough stock to fulfill the purchase.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity  # updates the quantity
        return total_price

    def __str__(self):
        promo_text = f" ({self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}{promo_text}"

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        pass  # quantity cannot be changed

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("quantity to buy must be greater than zero.")
        return self.price * quantity

    def __str__(self):
        return f"{self.name}, Price: ${self.price} (Non-stocked product)"


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("maximum must be greater than zero.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(
                f"cannot buy more than {self.maximum} of this product in one order."
            )
        return super().buy(quantity)

    def __str__(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity} (Max: {self.maximum} per order)"
