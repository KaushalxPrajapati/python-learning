# Logical Operators in Python (and, or, not)

is_logged_in = True
has_permission = False

# AND operator: True only if BOTH conditions are True
print("Can perform action (and):", is_logged_in and has_permission)

# OR operator: True if AT LEAST ONE condition is True
print("Has any access (or):", is_logged_in or has_permission)

# NOT operator: Reverses True to False and vice versa
print("Inverted login status (not):", not is_logged_in)
