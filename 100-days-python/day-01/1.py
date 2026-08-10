# Problem: Create a program that takes a student's marks as input and prints their result.

def result():
    try:
        while True:
            marks = int(input("Enter Student Marks: "))
            if marks < 0 or type(marks) == "str":
                return "Invalid"
            elif marks >= 90 and marks <= 100:
                return "Grade A"
            elif marks >= 75 and marks < 90:
                return "Grade B"
            elif marks >= 50 and marks < 75:
                return "Grade C"
            else:
                return "Failed!"
    except ValueError:
        print("Error...")


result()
print("hello")
