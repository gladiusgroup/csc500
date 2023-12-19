# List demo

# Create empty list
my_list = []

# Append some elements to the list
my_list.append("cessna")
my_list.append("piper")

# Insert an element at a specific index
my_list.insert(1, "mooney")

# Update an element by direct assignment
my_list[2] = "beechcraft"

# Print the current list
print("List after updates:", my_list)

# Remove an element using pop
popped_item = my_list.pop(1)
print("Popped item:", popped_item)
print("List after pop:", my_list)

# Remove an element using remove
my_list.remove("cessna")
print("List after removing 'cessna':", my_list)
