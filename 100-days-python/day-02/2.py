# Problem: Write a function called check_age(age) that takes a person's age
# and returns their category based on the following rules:
#
# - Age below 13       -> "Child"
# - Age 13 to 19       -> "Teenager"
# - Age 20 to 59       -> "Adult"
# - Age 60 or above    -> "Senior Citizen"
#
# Requirements:
# - Take the age from the user outside the function.
# - Pass the age to the function as an argument.
# - Use if / elif / else.
# - Use return to return the category.
# - Keep asking for another age after displaying the result.
#
# Example:
#
# Enter your age: 16
# Teenager
#
# Enter your age: 35
# Adult
#
# Enter your age: 65
# Senior Citizen


def check_age(age):
    if age < 13:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    elif age >= 20 and age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"


while True:
    age = int(input("Enter your age: "))
    print(check_age(age), "\n")
