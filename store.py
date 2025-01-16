from typing import List, Tuple
import products


class Store:
    """manages a collection of products in the store."""

    def __init__(self, product_list: List[products.Product]):
        """initializes the store with a list of products."""
        self.products = product_list

    def add_product(self, product: products.Product):
        """adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: products.Product):
        """removes a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """returns the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[products.Product]:
        """returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        """handles an order and returns the total price."""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


# test the store class
if __name__ == "__main__":
    product_list = [
        products.Product("macbook air m2", price=1450, quantity=100),
        products.Product("bose quietcomfort earbuds", price=250, quantity=500),
    ]
    store = Store(product_list)
    print(store.get_total_quantity())  # expected: 600
