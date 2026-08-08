def is_prime():
    while True:
        num = int(input("Enter the number: "))
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print("Number is not prime")
                    break
            else:
                print("Number is prime")
        else:
            print("Number is not prime")

        x = input("Press 'enter' to continue or any other key to exit: ")
        if x == "":  # if empty string
            print()
            continue
        else:
            break


is_prime()
