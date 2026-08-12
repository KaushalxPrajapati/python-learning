# Problem: Write a function called find_larger(a, b) that takes two numbers
# and returns:
#
# - "First number is larger" if a is greater than b
# - "Second number is larger" if b is greater than a
# - "Both numbers are equal" if a and b are equal
#
# Requirements:
# - Take both numbers from the user outside the function.
# - Pass both numbers to the function as arguments.
# - Use if / elif / else.
# - Use return.
# - Keep asking for another pair of numbers after displaying the result.
#
# Example:
#
# Enter first number: 25
# Enter second number: 10
# First number is larger
#
# Enter first number: 7
# Enter second number: 19
# Second number is larger
#
# Enter first number: 15
# Enter second number: 15
# Both numbers are equal


def find_larger(a, b):
    if a > b:
        return f"{a} > {b}"
    elif a < b:
        return f"{a} < {b}"
    else:
        return f"{a} = {b}"


while True:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    print(find_larger(num1, num2), "\n")
