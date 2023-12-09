class ItemToPurchase:
    # Ensure default values are set
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    #Print the cost of the item
    def print_item_cost(self):
        return self.item_quantity * self.item_price

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

def main():
    items = []
    #Limit items to 2
    for i in range(2):
        print(f"Item {i + 1}:")
        name = input("Enter the item name: ")
        price = get_validated_input("Enter the item price: ", float)
        quantity = get_validated_input("Enter the item quantity: ", int)
        items.append(ItemToPurchase(name, price, quantity))
    #Calculate the total cost and print it
    total_cost = sum(item.print_item_cost() for item in items)
    print(f"Total: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
