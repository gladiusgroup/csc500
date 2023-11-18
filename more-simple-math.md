
# More Simple Math

## This is what I get for going too fast and not reading the instructions carefully, I need two scripts, not one, too late nowm we're sticking with our class.

class MoreBasicMath

    In the class, create two methods for the second two math functions and round the result so it's not out of control
    multiply_method

    divide_method
    Continuing with the theme of never trusting the user, if they're trying to divide by zero, we need to stop them

## Never trust the user to follow instructions, did they give us actual numbers?

    if num1 or num2 not a number
    print complaint to user
    return

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
    multiply_result = multiply_method num1 * num2
    if num2 not a zero
        divide_result = divide_method num1 / num2

    Tell the user what the output was
    print words, multiply_result
    print words, divide_result

normal main handling stuff
