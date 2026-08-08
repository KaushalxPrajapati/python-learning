def calculator(a, b):
    if operator_choice == 1:
        return a + b
    elif operator_choice == 2:
        return a - b
    elif operator_choice == 3:
        return a * b
    elif operator_choice == 4:
        return round(a / b, 2)
    elif operator_choice == 5:
        return a // b
    elif operator_choice == 6:
        return a % b
    elif operator_choice == 7:
        return a**b
    else:
        invalid_msg = "Please choose the correct operator"
        return invalid_msg


if __name__ == "__main__":
    while True:
        print("""
1. Add(+)")
2. Subtract(-)")
3. Multiply(*)")
4. Divide(/)")
5. Floor(//)")
6. Floor(%)")
7. Exponent(*)
        """)
        try:
            operator_choice = int(input("Select an operation from above: "))
            a = int(input("Enter 1st no. "))
            b = int(input("Enter 2nd no. "))
            print(calculator(a, b))
        except:
            choice = input("Enter to continue or type exit to close the program ")
            if choice.lower() != "exit":
                continue
            else:
                break
