# Problem: Write a function called calculate_discount(price) that takes the price
# of a product and returns the applicable discount category.
#
# Discount Rules:
# - Price >= 5000  -> "20% Discount"
# - Price >= 2000  -> "10% Discount"
# - Price >= 1000  -> "5% Discount"
# - Price < 1000   -> "No Discount"
#
# Requirements:
# - Take the price from the user outside the function.
# - Pass the price to the function as an argument.
# - Use if / elif / else.
# - Use return to return the result.
# - Keep asking for another price after displaying the result.
#
# Example:
#
# Enter product price: 3500
# 10% Discount
#
# Enter product price: 800
# No Discount
#
# Enter product price: 6000
# 20% Discount


def calculate_discount(price):
    if price >= 5000:
        discount = 0.20
    elif price >= 2000:
        discount = 0.10
    elif price >= 1000:
        discount = 0.05
    else:
        discount = 0

    price = price - discount * price
    print(f"Amount to Pay: ₹{price}")


while True:
    price = int(input("Enter the price of the product: "))
    calculate_discount(price)
