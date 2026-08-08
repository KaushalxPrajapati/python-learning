def number_pyramid():
    n = int(input("Enter the number of rows you want: "))

    # First loop for printing the increasing pattern
    for i in range(1, n + 1):  # Loop through rows from 1 to n
        for j in range(1, i + 1):  # Loop through columns from 1 to i
            print(j, end="")  # Print the column value without newline
        print()  # Move to the next line after printing all columns

    # Second loop for printing the decreasing pattern
    for k in range(1, n + 1):  # Loop through rows from 1 to n
        for l in range(1, n + 1 - k):  # Loop through columns from 1 to n-k
            print(l, end="")  # Print the column value without newline
        print()  # Move to the next line after printing all columns


number_pyramid()
