def print_diamond():
    # Upper half of the diamond
    n = int(input("Enter the number of n you want: "))
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()

    # Lower half of the diamond
    for i in range(n - 1, 0, -1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()


print_diamond()
