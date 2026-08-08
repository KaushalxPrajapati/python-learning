# Type Casting (Converting data types in Python)

# String to Integer
number_str = "100"
number_int = int(number_str)
print("Converted String to Int:", number_int, "| Type:", type(number_int))

# Integer to Float
val_int = 50
val_float = float(val_int)
print("Converted Int to Float:", val_float, "| Type:", type(val_float))

# Float to Integer (removes decimals)
price = 99.99
price_int = int(price)
print("Converted Float to Int:", price_int, "| Type:", type(price_int))

# Number to String
score = 95
score_str = str(score)
print("Converted Int to String:", score_str, "| Type:", type(score_str))
