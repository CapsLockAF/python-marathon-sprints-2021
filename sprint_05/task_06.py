# Write  the function divide(numerator, denominator) the two input
# parameters of which are numbers. The function returns the result
# of dividing two numbers.
#  in case of correct data the function should be displayed
#  the corresponding message – "Result is  numerator / denominator"
# in the case of division by zero the function should be displayed
# the corresponding message – "Oops, numerator / denominator,
# division by zero is error!!!"
#
# in the case of incorrect data the function should be displayed
# the message – "Value Error! You did not enter a number!"
# Note: in the function you must use the "try except" construct.
#
# Function example:
# divide(8, 16)     "Result is 0.5"
# divide (5, 0)    "Oops, 5 / 0 denominator, division by zero is error!!!"
# divide_number("25", 5)    "Value Error! You did not enter a number!"
# divide_number("abc", 9)   "Value Error! You did not enter a number!"

def divide(numerator, denominator):
    try:
        return f"Result is {numerator/denominator}"
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except TypeError:
        return "Value Error! You did not enter a number!"
