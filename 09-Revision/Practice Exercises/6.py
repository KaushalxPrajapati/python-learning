num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

found = False

for i in range(1, 1001):
    if i % num1 == 0 and i % num2 == 0:
        print(i)
        found = True
        break

if not found:
    print("No number found between 1 and 1000 that is divisible by both.")
