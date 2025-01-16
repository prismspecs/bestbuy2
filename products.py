class Product:
    """represents a product in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        """initializes the product with a name, price, and quantity."""
        # validate input and initialize instance variables
        if not name.strip():
            raise ValueError("name cannot be empty.")
        if price < 0:
            raise ValueError("price cannot be negative.")
        if quantity < 0:
            raise ValueError("quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # products start as active

    def get_quantity(self) -> float:
        """returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """sets the quantity of the product. deactivates if quantity is 0."""
        if quantity < 0:
            raise ValueError("quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()  # deactivate when stock is zero

    def is_active(self) -> bool:
        """returns true if the product is active."""
        return self.active

    def activate(self):
        """activates the product."""
        self.active = True

    def deactivate(self):
        """deactivates the product."""
        self.active = False

    def show(self) -> str:
        """returns a string representation of the product."""
        return f"{self.name}, price: {self.price}, quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """handles the purchase of a given quantity."""
        if quantity <= 0:
            raise ValueError("quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("not enough stock to fulfill the purchase.")
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


# test the product class
if __name__ == "__main__":
    bose = Product("bose quietcomfort earbuds", price=250, quantity=500)
    mac = Product("macbook air m2", price=1450, quantity=100)

    print(bose.buy(50))  # expected: 12500
    print(mac.buy(100))  # expected: 145000
    print(mac.is_active())  # expected: false
    print(
        bose.show()
    )  # expected: "bose quietcomfort earbuds, price: 250, quantity: 450"
