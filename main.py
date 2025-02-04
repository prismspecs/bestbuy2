import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

# create a store instance with the initial products
best_buy = store.Store(product_list)


def handle_order(store_object):
    """handles placing an order in the store."""
    # explain to the user how to enter an order
    print(
        "\nenter your order. type the product name and quantity separated by a comma."
    )
    print("example: macbook air m2, 1")
    print("type 'done' when you are finished.")

    # list to hold the user's order
    shopping_list = []
    while True:
        # get input from the user
        order_input = input("order item (or 'done'): ").strip()
        if order_input.lower() == "done":
            # stop taking input when the user types 'done'
            break
        try:
            # split input into product name and quantity
            name, quantity = order_input.split(",", 1)
            name = name.strip()
            quantity = int(quantity.strip())

            # find the product in the store's active products
            product = next(
                (p for p in store_object.get_all_products() if p.name == name), None
            )
            if product:
                shopping_list.append((product, quantity))
            else:
                print(f"product '{name}' not found. please check the product name.")
        except ValueError:
            # handle invalid input format
            print("invalid input. please enter in the format: product_name, quantity.")

    # process the order if the shopping list is not empty
    if shopping_list:
        try:
            total_price = store_object.order(shopping_list)
            print(f"\norder placed successfully! total price: {total_price} dollars.")
        except ValueError as e:
            # handle errors during the order
            print(f"order error: {e}")


def handle_choice(choice, store_object):
    """processes the user's menu choice."""
    if choice == "1":
        # option to list all products in the store
        print("\nproducts in the store:")
        for product in store_object.get_all_products():
            print(product)
    elif choice == "2":
        # option to show the total quantity of all products
        print(
            f"\ntotal quantity of items in store: {store_object.get_total_quantity()}"
        )
    elif choice == "3":
        # option to make an order
        handle_order(store_object)
    elif choice == "4":
        # option to quit the program
        print("thank you for visiting the store. goodbye!")
        return False
    else:
        # handle invalid menu choices
        print("invalid choice. please enter a number between 1 and 4.")
    return True


def start(store_object):
    """starts the user interface loop."""
    while True:
        # display the menu options to the user
        print("\nwelcome to the store! please choose an option:")
        print("1. list all products in store")
        print("2. show total amount in store")
        print("3. make an order")
        print("4. quit")

        # get the user's choice and process it
        if not handle_choice(input("enter your choice: "), store_object):
            break


# start the program if this file is run directly
if __name__ == "__main__":
    start(best_buy)
