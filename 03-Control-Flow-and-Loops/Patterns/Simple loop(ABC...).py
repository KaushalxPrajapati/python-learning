def print_alphabet_pattern():
    # Initialize the count for the number of letters to be printed in each row
    count = 1
    
    # Start with the first letter of the alphabet 'A'
    letter = ord('A')
    
    # Loop until we reach the letter 'Z'
    while letter <= ord('Z'):
        # Loop 'count' times to print the required number of letters in each row
        for _ in range(count):
            # Check if we have printed all letters up to 'Z'
            if letter > ord('Z'):
                break
            # Print the current letter and move to the next letter
            print(chr(letter), end=" ")
            letter += 1
        # Move to the next line after printing all letters in the row
        print()
        # Increment the count to print one more letter in the next row
        count += 1


print_alphabet_pattern()


'''
A
B C
D E F
G H I J
K L M N O
P Q R S T U
V W X Y Z
'''
