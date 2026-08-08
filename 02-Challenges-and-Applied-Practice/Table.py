# This program generates "MULTIPLICATION TABLE" tables within a specified range
def table():
    start = int(input("Enter starting no. "))
    end = int(input("Enter ending no. "))
    for i in range(start, end + 1):
        for j in range(1, 11):
            print(i, "x", j, "=", i * j)
        print()


while True:
    table()
    choice = input("Press Enter to continue or type anything else to exit:")  # If the choice is not an empty string ( means user typed something)
    if choice != "":  # Empty string!
        break  # Exit the loop, as the user want to end the program.
