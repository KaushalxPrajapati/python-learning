def meNmyEdu():
    while True:
        year = int(input("Enter year: "))

        # Before 2005
        if year < 2005:
            print("Are you mad, bro?!?")
            print()
            continue

        # Display the appropriate educational stage based on the year
        if year >= 2005:
            age = year - 2005
            print("Age:", age)

            # Gap
            if year >= 2005 and year < 2008:
                if year == 2005:
                    print("Just born")
                else:
                    print("Not started yet!")

            # Kindergarten times
            elif year >= 2008 and year <= 2009:
                if year % 100 == 8:
                    print("You were in Pre-Nursery class")
                else:
                    print("You were in Nursery class")

            # Junior High School times
            elif year >= 2010 and year < 2020:
                s = year % 100
                if s == 10:
                    Class = "L.K.G"
                elif s == 11:
                    Class = "U.K.G"
                elif s == 12:
                    Class = "1st"
                elif s == 13:
                    Class = "2nd"
                elif s == 14:
                    Class = "3rd"
                else:
                    Class = str(s - 11) + "th"
                print("You were in", Class, "class")

            # Senior High School times
            elif year >= 2020 and year < 2024:
                s = year % 100
                Class = str(s - 11) + "th"
                print("You were in", Class, "class")

            # Extra
            elif year >= 2024 and year <= 2028:
                print(
                    "Congratulations! You have completed Senior High School and now in college."
                )

            # After 2028
            else:
                print("You are living your life😊")

        print()

        # Ask the user if they want to continue or exit
        user_input = input("Press 'enter' to continue or any other key to exit: ")
        print()
        if user_input != "":
            print("Exiting...")
            break


meNmyEdu()
