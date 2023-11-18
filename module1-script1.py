# python 3.6 script to add and subtract two numbers

class BasicMath:
    def add(self, num1, num2):
        result = num1 + num2
        return round(result, 2)

    def subtract(self, num1, num2):
        result = num1 - num2
        return round(result, 2)

def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def main():
    
    # Print a welcome message
    print("This program will add and subtract two numbers.")
        
    # Get input and validate it
    num1_str = input("Enter the first number (num1): ")
    num2_str = input("Enter the second number (num2): ")

    if not is_number(num1_str) or not is_number(num2_str):
        print("Please enter valid numbers.")
        return

    num1 = float(num1_str)
    num2 = float(num2_str)

    # Create an instance of the BasicMath class
    basic_calc = BasicMath()

    # Performing addition and subtraction
    sum_result = basic_calc.add(num1, num2)
    subtraction_result = basic_calc.subtract(num1, num2)

    # Displaying the results
    print("The addition of the two numbers is:", sum_result)
    print("The subtraction of the two numbers is:", subtraction_result)

if __name__ == "__main__":
    main()
