first_name = "Kaushal"
last_name = "Prajapati"
name = "Tony Stark"

# string operations
print(first_name.upper())  # KAUSHAL
print(first_name.lower())  # kaushal

# find method
print(first_name.find("l"))  # 6
print(last_name.find("P"))  # 0
print(name.find("x"))  # -1

# replace
print(first_name.replace("Kaushal", "Mr."), last_name)
print(name.replace(name[0:4], "Mr."))


print("----------------------------------------------------------")

# Arithmatic Operators
print(5 + 3) # 8
print(5 - 3) # 2
print(5 * 3) # 15
print(5 / 3) # 1.666666666667
print(5 // 3) # 1
print(5 % 3) # 2


# Assignment Operators
x = 10
print(x)

x += 5
print(x)
