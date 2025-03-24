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
    print("\nEnter your order using the product number and quantity.")
    print("Example: 1, 2 (for 2 units of product #1)")
    print("Type 'done' when you are finished.")

    # list to hold the user's order
    shopping_list = []
    while True:
        # get input from the user
        order_input = input("Order item (or 'done'): ").strip()
        if order_input.lower() == "done":
            # stop taking input when the user types 'done'
            break
        try:
            # split input into product number and quantity
            product_num, quantity = order_input.split(",", 1)
            product_num = int(product_num.strip())
            quantity = int(quantity.strip())

            # get all active products
            active_products = store_object.get_all_products()
            if 1 <= product_num <= len(active_products):
                product = active_products[product_num - 1]
                shopping_list.append((product, quantity))
            else:
                print(f"Product number '{product_num}' not found. Please check the product number.")
        except ValueError:
            # handle invalid input format
            print("Invalid input. Please enter in the format: product_number, quantity.")

    # process the order if the shopping list is not empty
    if shopping_list:
        try:
            total_price = store_object.order(shopping_list)
            print(f"\nOrder placed successfully! Total price: ${total_price:.2f}")
        except ValueError as e:
            # handle errors during the order
            print(f"Order error: {e}")


def handle_choice(choice, store_object):
    """processes the user's menu choice."""
    if choice == "1":
        # option to list all products in the store
        print("\nProducts in the store:")
        for idx, product in enumerate(store_object.get_all_products(), 1):
            print(f"{idx}. {product}")
    elif choice == "2":
        # option to show the total quantity of all products
        print(f"\nTotal quantity of items in store: {store_object.get_total_quantity()}")
    elif choice == "3":
        # option to make an order
        handle_order(store_object)
    elif choice == "4":
        # option to quit the program
        print("Thank you for visiting the store. Goodbye!")
        return False
    else:
        # handle invalid menu choices
        print("Invalid choice. Please enter a number between 1 and 4.")
    return True


def start(store_object):
    """starts the user interface loop."""
    while True:
        # display the menu options to the user
        print("\nWelcome to the store! Please choose an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        # get the user's choice and process it
        if not handle_choice(input("Enter your choice: "), store_object):
            break


# start the program if this file is run directly
if __name__ == "__main__":
    start(best_buy)
