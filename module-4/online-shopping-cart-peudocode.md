# Online Shopping Cart

## Class: ItemToPurchase

- Attributes:
  - item_name: string
  - item_price: float
  - item_quantity: int

- Constructor:
  - Initialize item_name to none, item_price to 0.0, item_quantity to 0

- Method:
  - print_item_cost: Returns total cost item_price * item_quantity

## Main

1. Initialize an empty list called items

2. Loop twice (two items only):
   a. Prompt user for item name, price, and quantity
   b. Convert price to float and quantity to int
   c. Create an instance of ItemToPurchase class with the values
   d. Add this instance to the items list
3. Calculate the total cost the items list
4. Print the total cost

## Execution Flow

- main
