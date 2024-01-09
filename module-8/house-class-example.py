# House Class Exmaple
class House:
    def __init__(self, exterior_type='Brick', number_of_floors=2, builder='Unknown'):
        # Initializes a new House object with default values unless otherwise specified.
        self.exterior_type = exterior_type
        self.number_of_floors = number_of_floors
        self.builder = builder

    def display_house_info(self):
        # Prints the details of the house.
        print(f"House Details:\nExterior: {self.exterior_type}\nFloors: {self.number_of_floors}\nBuilder: {self.builder}")

# Example usage
my_house = House(exterior_type='Wood', number_of_floors=3, builder='Acme Builders')
my_house.display_house_info()
