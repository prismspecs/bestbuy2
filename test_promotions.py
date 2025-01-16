from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
]

# create promotion catalog
second_half_price = SecondHalfPrice("Second Half Price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% Off!", percent=30)

# add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

# test promotions
print(product_list[0].buy(3))  # should calculate with second half price
print(product_list[1].buy(3))  # should calculate with third one free
print(product_list[3].buy(1))  # should apply 30% discount
