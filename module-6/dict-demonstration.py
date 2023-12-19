#Dictionary demo

# Create empty dictionary
my_dict = {}

# Insert elements
my_dict["cessna"] = 5
my_dict["piper"] = 3
my_dict["mooney"] = 2

# Update the value existing key
my_dict["cessna"] = 4

# Print the current dictionary
print("Dictionary after updates:", my_dict)

# Remove an element using pop
popped_value = my_dict.pop("piper")
print("Popped value:", popped_value)
print("Dictionary after pop:", my_dict)

# Remove an element using del
del my_dict["mooney"]
print("Dictionary after deleting 'mooney':", my_dict)
