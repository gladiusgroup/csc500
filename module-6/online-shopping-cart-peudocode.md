# Online Shopping Cart with new class and markdown

## Class: ItemToPurchase

- **Attributes**:
  - `item_name`: string
  - `item_price`: float
  - `item_quantity`: int
  - `description` : string

- **Constructor**:
  - Initialize `item_name` none, `item_price` of 0.0, `item_quantity` of 0, `description` of none

- **Method**:
  - `print_item_cost`: Returns total cost `item_price * item_quantity`

## Class: ShoppingCart

- **Attributes**:
  - `customer_name`: string
  - `current_date`: string
  - `cart_items`: list of ItemToPurchase objects

- **Constructor**:
  - Initialize `customer_name`, `current_date`, and an empty `cart_items` list

- **Methods**:
  - `add_item`: Adds an ItemToPurchase to the `cart_items` list
  - `remove_item`: Removes an item by name from `cart_items`
  - `modify_item`: Modifies details of an existing ItemToPurchase in `cart_items`
  - `get_num_items_in_cart`: Returns the total quantity of items in the cart
  - `get_cost_of_cart`: Returns the total cost of items in the cart
  - `print_total`: Outputs information about the cart
     - customer name - date
     - number of items
     - item name quantity @ price = sum
     - total cost of what is in the cart
  - `print_descriptions`: Outputs descriptions of each item in the cart

## Function: get_validated_input

- Prompts user for valid data
- Try-except to catch type conversion errors
- Check for negative numbers
- Return validated input

- **Parameters**:
  - `prompt_message`: string
  - `value_type`

## Function: print_menu

- Display menu and options
  - 'a': "Add item to cart",
  - 'r': "Remove item from cart",
  - 'c': "Change item quantity",
  - 'i': "Output items' descriptions",
  - 'o': "Output shopping cart",
  - 'q': "Quit"
- Prompt user for selection
- Call apprpriate class and method based on selection
- Validate input and handle unfinished selections
- Loop until they exit

## Main

1. Initialize a ShoppingCart instance with user-provided customer name and date.

2. Initialize an empty list called items to hold user's shopping items

3. Loop twice (for two items only):
   a. For each attribute (name, price, quantity):
      i. Use the `get_validated_input` function to ensure correct input type:
         - For price, ensure it's a valid float.
         - For quantity, ensure it's a valid integer.
      ii. Prompt user for item name (string input can be taken directly).
      iii. Create an instance of ItemToPurchase class with validated values.
      iv. Use the `add_item` method of ShoppingCart to add this instance to the cart.

4. Calculate the total cost by summing the costs of items in the list.

5. Print the total cost from contents of the list.

6. Add the items from the list to the cart

7. Call `print_menu

## Execution Flow

- Call `main` function when the script is executed.
