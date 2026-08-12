# Problem: Create a program that takes a student's marks as input and prints their result.


def result():
    while True:
        try:
            marks = int(input("Enter Student Marks: "))

            if marks < 0 or marks > 100:
                print("Invalid marks. Enter marks between 0 and 100.")
                continue

            if marks >= 90:
                print("Grade A")

            elif marks >= 75:
                print("Grade B")

            elif marks >= 50:
                print("Grade C")

            else:
                print("Failed!")

        except ValueError:
            print("Invalid input. Please enter a number.")


result()
