# Problem: Write a function called check_divisibility(num) that takes an integer
# and returns:
#
# - "Divisible by both 3 and 5" if the number is divisible by both 3 and 5
# - "Divisible by 3" if the number is divisible only by 3
# - "Divisible by 5" if the number is divisible only by 5
# - "Not divisible by 3 or 5" if the number is divisible by neither
#
# Requirements:
# - Take the number from the user outside the function.
# - Pass the number to the function as an argument.
# - Use if / elif / else.
# - Use the modulo (%) operator.
# - Use return.
# - Keep asking for another number after displaying the result.
#
# Example:
#
# Enter a number: 15
# Divisible by both 3 and 5
#
# Enter a number: 9
# Divisible by 3
#
# Enter a number: 20
# Divisible by 5
#
# Enter a number: 7
# Not divisible by 3 or 5


def check_divisibility(a):
    if a % 3 == 0 and a % 5 == 0:
        return "Divisible by both 3 and 5"
    elif a % 3 == 0:
        return "Divisible only by 3"
    elif a % 5 == 0:
        return "Divisible only by 5"
    else:
        return "Not divisible by 3 or 5"


while True:
    num = int(input("Enter an Integer: "))
    print(check_divisibility(num), "\n")
