# simple-math.md

## Looks like there are multiple math functions, let's group them togehter as methods ina class

class BasicMath

    #In the class, create two methods for the first two math functions and round the result so it's not out of control
    sum_method
    substract_method

## Never trust the user to follow instructions, did they give us actual numbers?

valid_number_function

main
    print words to the user re: what we're doing

    Get the input from the user
    num1
    num2

    Check the input
    if num1 or num2 not a number
    print complaint to user
    return

    Convert the input values to floats
    num1 = float
    num2 = float

    Instantiate our class
    newclassinstance = BasicMath()

    Do some math
    sum_result = sum num1 + num2
    subtraction_result = subtract num1 - num2

    Tell the user what the output was
    print words, sum_result
    print words, subtraction_result

normal main handling stuff
