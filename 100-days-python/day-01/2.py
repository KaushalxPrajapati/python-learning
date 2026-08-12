# Problem: Write a function called check_number(num) that takes an integer and returns:
# "Positive" if the number is greater than 0
# "Negative" if the number is less than 0
# "Zero" if the number is exactly 0

def check_number(num):
    if num > 0:
        return "Positive(+)"
    elif num < 0:
        return "Negative(-)"
    else:
        return "Zero(0)"

while True:
    num = int(input("Enter an Integer Number: "))
    print(check_number(num))
