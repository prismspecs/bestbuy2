from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

# setup initial stock of inventory
mac = Product("MacBook Air M2", price=1450, quantity=100)
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
pixel = Product("Google Pixel 7", price=500, quantity=250)
windows = NonStockedProduct("Windows License", price=125)
shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

# create a promotion catalog
second_half_price = SecondHalfPrice("Second Half Price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% Off!", percent=30)

# add promotions to products
mac.set_promotion(second_half_price)
bose.set_promotion(third_one_free)
windows.set_promotion(thirty_percent)

# test product details
print(mac)  # MacBook Air M2, Price: $1450, Quantity: 100 (Second Half Price!)
print(bose)  # Bose QuietComfort Earbuds, Price: $250, Quantity: 500 (Third One Free!)
print(windows)  # Windows License, Price: $125 (30% Off!)

# test buying products with promotions
print(mac.buy(3))  # second half price: 1450 + 725 + 1450 = 3625
print(bose.buy(3))  # third one free: 250 + 250 + 0 = 500
print(windows.buy(2))  # 30% discount: 125 * 2 * 0.7 = 175.0

# test limited product purchase
print(shipping.buy(1))  # 10
try:
    print(shipping.buy(2))  # should raise an exception
except ValueError as e:
    print(e)
