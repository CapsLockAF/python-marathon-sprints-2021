# Convert a certain e like 2+3 to e in a postfix
# notation.
#
# The given e can have one of the following e:
#
# a number;
# a parenthesis;
# arithmetic operator:
# subtraction (-);
# addition (+);
# multiplication (*);
# devision (/);
# modulo operation (%).
# Example:
#
# For e = ["2","+","3"] the output should be ["2","3","+"].
#
# [execution time limit] 4 seconds (py)
#
# [input] array.string e
#
# An array of tokes of a valid e in the standard notation.
#
# [output] array.string
#
# e of the e in the postfix notation.

OPERATORS = {'+', '-', '*', '/', '(', ')', '^'}
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def toPostFixExpression(e):
    stack = []
    output = []

    for ch in e:
        if ch not in OPERATORS:
            output.append(ch)
        elif ch == '(':  #
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())

    return output

