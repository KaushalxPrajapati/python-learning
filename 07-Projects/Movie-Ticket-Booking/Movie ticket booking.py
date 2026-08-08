import mysql.connector as ms
from random import randint

con = ms.connect(host="localhost", user="root", password="123456")
c = con.cursor()

print("\n")
print("  " + "-" * 90)
print(" | >>>>>>>>>>>>>> Welcome To KP Cinemas [ KPC ] <<<<<<<<<<<<<< |")
print("  " + "-" * 90)
print("\n")

# Check existing databases and create 'library_app' if it does not exist
c.execute("create database if not exists kp_cinemas")
c.execute("use kp_cinemas")

# Create necessary tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS movies (
              S_NO INT PRIMARY KEY AUTO_INCREMENT,
              MOVIE_NAME VARCHAR(50),
              DATE VARCHAR(10),
              TIME VARCHAR(10),
              CHARGE INT)''')

c.execute('''CREATE TABLE IF NOT EXISTS Viewers (
              NAME VARCHAR(20),
              Ticket INT,
              MOVIE_NAME VARCHAR(50),
              SEAT_NO INT,
              PAID INT)''')

# Insert movies into the 'movies' table
movies_list = [
    (1, 'Hanu-Man', '22/01/2024', '11:55pm', 90),
    (2, 'Interstellar', '15/02/2024', '7:00pm', 300),
    (3, 'The Matrix', '08/03/2024', '5:00pm', 270),
    (4, 'Dangal', '21/04/2024', '5:30pm', 150),
    (5, '3 Idiots', '10/05/2024', '3:00pm', 120),
    (6, 'Man of Steel', '22/06/2024', '5:30pm', 240),
    (7, 'Aladdin', '17/07/2024', '6:00pm', 200),
    (8, 'RRR', '04/08/2024', '4:30pm', 250),
    (9, 'The Dark Knight', '12/09/2024', '5:30pm', 300),
    (10, 'The Lion King', '28/10/2024', '8:30pm', 280)]

for i in movies_list:
    c.execute('''INSERT IGNORE INTO movies VALUES (%s, %s, %s, %s, %s)''', i)
con.commit()


# SYSTEM PASSWORD LOGIN
def signin():
    '''Id = input("Enter Your id: ")
    password = input("Enter Your Password: ")
    if Id == "user" and password == "123":
        print("-----LOGIN SUCCESSFUL-----")
        options()
    else:
        print("\nIncorrect Id or password. Please try again.\n")
        signin()'''
    options()

def display_movies():
    print("\n\n *********** Available SHOWS *********** \n")
    c.execute("SELECT MOVIE_NAME FROM movies ORDER BY S_NO")  # Select movies in ascending order of S_NO
    count = 0
    for movie in c:
        count += 1
        print(str(count) + ")", movie[0])
    print()


def book_ticket():
    display_movies()
    # Assuming you are getting the choice from the user for the movie
    choice = int(input("\nSelect Movie To Book Ticket (Enter the number): "))

    # Check if the chosen movie number exists in the movies table
    c.execute("SELECT MOVIE_NAME, CHARGE FROM movies WHERE S_NO = %s", (choice,))
    result = c.fetchone()

    if result:
        # Your existing code for ticket booking
        vr = input("Viewer Name: ")
        t = int(input("Enter Number of Tickets: "))
        movie_name, charge = result[0], result[1]
        total_cost = t * charge  # Calculating the total cost based on charge per ticket
        seat_number = randint(1, 100)  # Generate a random seat number

        # Inserting data into Viewers table with correct PAID value
        c.execute('''INSERT INTO Viewers (NAME, Ticket, MOVIE_NAME, SEAT_NO, PAID) 
                VALUES (%s, %s, %s, %s, %s)''', (vr, t, movie_name, seat_number, total_cost))
        con.commit()
        print("TICKET BOOKED SUCCESSFULLY")
        options()
    else:
        print("Invalid movie selection.")
        options()


def view_bookings():
    c.execute('SELECT * FROM Viewers')
    bookings = c.fetchall()

    if not bookings:
        print('''You have no bookings. How about getting started?''')
    else:
        for booking in bookings:
            # Fetch the associated movie details from the database for each booking
            c.execute("SELECT CHARGE, TIME, DATE FROM movies WHERE MOVIE_NAME = %s", (booking[2],))
            movie_data = c.fetchone()

            if movie_data:
                has_booking = True  # Set the flag to indicate there is at least one booking

                movie_price = movie_data[0]  # Get the charge per ticket
                movie_timing = movie_data[1]  # Get the movie timing
                movie_date = movie_data[2]  # Get the movie date
                total_cost = booking[1] * movie_price  # Calculate total amount paid
                print('''
                ----------------------------------------------
                |                   Ticket                   |
                |--------------------------------------------|
                | Name: {}                                   |
                | Movie: {}                                  |
                | Date: {}                                   |
                | Timing: {}                                 |
                | Seat No.: {}                               |
                | Total Cost: {}                             |
                ----------------------------------------------
                '''.format(booking[0], booking[2], movie_date, movie_timing, booking[3], total_cost))

            else:
                print("Error fetching movie details for booking: {}".format(booking))

    options()



def cancel_booking():
    print("\n===== CANCEL BOOKING =====\n")
    name = input("Enter your name: ")
    movie = input("Enter the movie you want to cancel booking for: ")

    # Check if the booking exists for the provided name and movie
    c.execute("SELECT * FROM Viewers WHERE NAME = %s AND MOVIE_NAME = %s", (name, movie))
    booking = c.fetchone()

    if booking:
        # Fetch or iterate over the result set to avoid unread result error
        for string in c:
            pass
        # Now, delete the booking(s) from the Viewers table
        c.execute("DELETE FROM Viewers WHERE NAME = %s AND MOVIE_NAME = %s", (name, movie))
        con.commit()
        print("Booking Canceled Successfully.")
    else:
        print("No Booking Found!")

    options()



choice = None  # Initialize choice globally
def options():
    print('''\nOPTIONS

1. Display Available Movies
2. Book Ticket
3. View Your Bookings
4. Cancel Booking          
5. Exit
        \n\n''')
    
    global choice  # Access the global choice variable
    choice = input("Enter your choice: ")
    
    if choice == '1':
        display_movies()
    elif choice == '2':
        book_ticket()
    elif choice == '3':
        view_bookings()
    elif choice == '4':
        cancel_booking()
    elif choice == '5':
        print("Exiting...")
        con.close()
    else:
        print("Invalid choice. Please try again!")


# Start the sign-in process
if __name__ == "__main__":
    while True:
        signin()
        if choice == '5':  # Check if the user chose option 5 to exit the loop
            break