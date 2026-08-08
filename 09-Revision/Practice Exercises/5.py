# Method 1
for i in range(1, 51):
    if i == 15:
        continue
    elif i % 3 == 0:
        print(i)

print("-" * 100)

# Method 2
for i in range(3, 51, 3):
    if i == 15:
        continue
    else:
        print(i)

print("-" * 100)

# Method 3
for i in range(1, 51):
    if i % 3 == 0 and i != 15:
        print(i)

print("-" * 100)

# Method 4
for i in range(3, 51, 3):
    if i != 15:
        print(i)
