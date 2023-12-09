# Online Shopping Cart

## Class: ItemToPurchase

- Attributes:
  - item_name: string
  - item_price: float
  - item_quantity: int

- Constructor:
  - Initialize item_name none, item_price of 0.0, item_quantity of 0

- Method:
  - print_item_cost: Returns total cost item_price * item_quantity

## Function: get_validated_input

- prompts user for valid
- try-except to catch type conversion errors
- return validated input

- Parameters:
  - prompt_message: string
  - value_type

## Main

1. Initialize an empty list called items.

2. Loop twice (for two items):
   a. For each attribute (name, price, quantity):
      i. Use the get_validated_input function to ensure correct input type:
         - For price, ensure it's a valid float.
         - For quantity, ensure it's a valid integer.
      ii. Prompt user for item name (string input can be taken directly).
      iii. Create an instance of ItemToPurchase class with validated values.
      iv. Add this instance to the items list.
3. Calculate the total cost by summing the costs of items in the list.
4. Print the total cost.

## Execution Flow

- Call main function when the script is executed.
