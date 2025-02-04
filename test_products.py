import pytest
from products import Product


# test that creating a normal product works
def test_create_product_normal():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True


# test that creating a product with invalid details raises exceptions
def test_create_product_invalid_details():
    # test empty name
    with pytest.raises(ValueError, match="name cannot be empty."):
        Product("", price=1450, quantity=100)

    # test negative price
    with pytest.raises(ValueError, match="price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)

    # test negative quantity
    with pytest.raises(ValueError, match="quantity cannot be negative."):
        Product("MacBook Air M2", price=1450, quantity=-5)


# test that when a product reaches 0 quantity, it becomes inactive
def test_product_becomes_inactive_at_zero_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.set_quantity(0)
    assert product.is_active() is False


# test that product purchase modifies the quantity and returns the correct output
def test_product_purchase_modifies_quantity_and_returns_correct_output():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(5)
    assert total_price == 1450 * 5
    assert product.quantity == 95


# test that buying a larger quantity than available raises an exception
def test_buying_larger_quantity_than_exists_raises_exception():
    product = Product("MacBook Air M2", price=1450, quantity=10)
    with pytest.raises(ValueError, match="not enough stock to fulfill the purchase."):
        product.buy(15)


if __name__ == "__main__":
    pytest.main()
