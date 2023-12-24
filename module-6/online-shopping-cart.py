import datetime

class ItemToPurchase:
    # Ensure default values are set
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Print the cost of the item
    def print_item_cost(self):
        return self.item_quantity * self.item_price

class ShoppingCart:
    # Ensure default values are set
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Adds an item to the cart
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    # Removes item from the cart
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    # Modify an existing item in the cart
    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    # Returns the total quantity of all items in the cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    # Returns the total cost of items in the cart
    def get_cost_of_cart(self):
        return sum(item.print_item_cost() for item in self.cart_items)

    # Prints the total of items in the cart along with their descriptions
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            total_item_cost = item.print_item_cost()
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${total_item_cost:.2f}")
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Total: ${total_cost:.2f}")

    # Prints each item's description
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


#Always the check the user's input
def get_validated_input(prompt_message, value_type):
    while True:
        try:
            #Check for proper input type
            value = value_type(input(prompt_message))
            #Make sure it's not negative
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please try again.")

def print_menu(shopping_cart):
    menu_options = {
        'a': "Add item to cart",
        'r': "Remove item from cart",
        'c': "Change item quantity",
        'i': "Output items' descriptions",
        'o': "Output shopping cart",
        'q': "Quit"
    }

    while True:
        print("\nMENU")
        for key, value in menu_options.items():
            print(f"{key} - {value}")
        choice = input("Choose an option: ").lower()

        if choice == 'q':
            confirm = input("Are you sure you want to quit? (Y/N): ").lower()
            if confirm == 'yes' or confirm == 'y':
                print("Goodbye, thanks for shopping with us!\n")
                break
            else:
                print("Invalid option. Returning to main menu.\n")
                continue
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        # Further options to be implemented later
        else:
            print("Invalid option. Please try again.\n")


def main():
    # Instantiate cart and get customer info
    customer_name = input("Enter customer's name: ")
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    cart = ShoppingCart(customer_name, current_date)
    items = []
    # Get item info from customer and limit items to 2
    for i in range(2):
        print(f"Item {i + 1}:")
        name = input("Enter the item name: ")
        price = get_validated_input("Enter the item price: ", float)
        quantity = get_validated_input("Enter the item quantity: ", int)
        description = input("Enter the item description: ")
        items.append(ItemToPurchase(name, price, quantity, description))

    # Calculate the total cost and print it
    total_cost = sum(item.print_item_cost() for item in items)
    print(f"\nTotal: ${total_cost:.2f}")

    # Add the items to the cart
    for item in items:
        cart.add_item(item)

    # Display the menu
    print_menu(cart)

if __name__ == "__main__":
    main()

