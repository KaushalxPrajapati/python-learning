# Calculates and displays the actual available storage (as the computer would show it) and also the discrepancy between the user input and the displayed storage.
import math

def convert():
    gb = int(input("Enter value in GB: "))
    byte = gb * (10 ** 9)  # Convert to bytes

    # Calculating what computer will display available storage to the user
    disp = byte / (1024 ** 3)
    print("Computer will display", round(disp, 2), "GB as available storage")

    # Calculate discrepancy
    disc = abs(gb - disp)
    print("Discrepancy: ", round(disc, 2), 'GB')

    # Want to continue?
    while True:
        choice = input("Press enter to continue or else to exit: \n") # If the choice is not an empty string ( means user typed something)
        if choice != "": 
            break  # Exit the loop, as the user want to end the program.
        else:
            convert()
        
convert()
