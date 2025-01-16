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

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # promotion applied to the product

    def get_quantity(self) -> float:
        # returns the current quantity of the product
        return self.quantity

    def set_quantity(self, quantity: int):
        # sets the quantity of the product. deactivates if quantity is 0
        if quantity < 0:
            raise ValueError("quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        # returns true if the product is active
        return self.active

    def activate(self):
        # activates the product
        self.active = True

    def deactivate(self):
        # deactivates the product
        self.active = False

    def set_promotion(self, promotion):
        # sets a promotion for the product
        self.promotion = promotion

    def show(self) -> str:
        # returns a string representation of the product, including its promotion
        promo_text = f" ({self.promotion.name})" if self.promotion else ""
        return (
            f"{self.name}, price: {self.price}, quantity: {self.quantity}{promo_text}"
        )

    def buy(self, quantity: int) -> float:
        # handles the purchase of a given quantity
        if quantity <= 0:
            raise ValueError("quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("not enough stock to fulfill the purchase.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    # represents a non-stocked product in the store

    def __init__(self, name: str, price: float):
        # initializes a non-stocked product with a name and price
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        # non-stocked products always have quantity 0, so this does nothing
        pass

    def buy(self, quantity: int) -> float:
        # allows purchase of any quantity since stock is not tracked
        if quantity <= 0:
            raise ValueError("quantity to buy must be greater than zero.")
        return self.price * quantity

    def show(self) -> str:
        # returns a string representation of the non-stocked product
        return f"{self.name}, price: {self.price} (non-stocked product)"


class LimitedProduct(Product):
    # represents a product with a maximum quantity allowed per order

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        # initializes a limited product with a maximum purchase limit
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("maximum purchase limit must be greater than zero.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        # allows purchase only if the quantity does not exceed the maximum limit
        if quantity > self.maximum:
            raise ValueError(
                f"cannot buy more than {self.maximum} of this product in one order."
            )
        return super().buy(quantity)

    def show(self) -> str:
        # returns a string representation of the limited product
        return f"{self.name}, price: {self.price}, quantity: {self.quantity} (maximum: {self.maximum} per order)"
