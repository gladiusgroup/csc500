# python 3.6 script to multiply and divide two numbers

class MoreBasicMath:
    def multiply(self, num1, num2):
        result = num1 * num2
        return round(result, 2)

    def divide(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            return round(result, 2)
        else:
            print("Cannot divide by zero")
            return

def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def main():
    
    # Print a welcome message
    print("This program will multiply and divide two numbers.")
        
    # Get input and validate it
    num1_str = input("Enter the first number (num1): ")
    num2_str = input("Enter the second number (num2): ")

    if not is_number(num1_str) or not is_number(num2_str):
        print("Please enter valid numbers.")
        return

    num1 = float(num1_str)
    num2 = float(num2_str)

    # Create an instance of the BasicMath class
    more_basic_calc = MoreBasicMath()

    # Performing addition and subtraction
    multiply_result = more_basic_calc.multiply(num1, num2)
    divide_result = more_basic_calc.divide(num1, num2)

    # Displaying the results
    print("The multiplication of the two numbers is:", multiply_result)
    print("The division of the two numbers is:", divide_result)

if __name__ == "__main__":
    main()
