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

    # property for name
    @property
    def name(self):
        return self._name

    # property for price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative.")
        self._price = value

    # property for quantity
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

        self.quantity -= quantity  # updates the quantity
        return total_price

    def __str__(self):
        # string representation for the product
        promo_text = f" ({self.promotion.name})" if self.promotion else ""
        return (
            f"{self.name}, Price: ${self.price} Quantity: {self.quantity}{promo_text}"
        )

    def __gt__(self, other):
        # compares products based on price
        return self.price > other.price

    def __lt__(self, other):
        # compares products based on price
        return self.price < other.price
