import mysql.connector as mysql
import random
import datetime

# Establish connection to MySQL database
try:
    con = mysql.connect(host="localhost", user="root", password="123456")
    cursor = con.cursor()
except Exception as e:
    print("Error:", e)
    exit()

print('''
***************************************************************************************
                                FLIGHT MANAGEMENT SYSTEM                               
***************************************************************************************
WELCOME TO OUR FLIGHT BOOKING SYSTEM
Explore, Book, and Manage Your Flights Effortlessly!
''')

# Check existing databases and create 'FMS' if it does not exist
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS FMS")
    cursor.execute("USE FMS")
except mysql.Error as e:
    print("Error:", e)

# Creating necessary tables in the database
def create_tables():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS flights(
                       flight_number INT,
                       airline VARCHAR(100),
                       origin VARCHAR(100),
                       destination VARCHAR(100),
                       departure_date DATE,
                       arrival_time TIME,
                       departure_time TIME,
                       available_seats INT,
                       cost INT,  # New column for flight cost
                       INDEX idx_flight_number (flight_number) )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS bookings(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       passenger_name VARCHAR(20),
                       flight_number INT,
                       airline  VARCHAR(20),
                       origin VARCHAR(20),
                       destination VARCHAR(20),
                       departure_date DATE,
                       arrival_time TIME,
                       departure_time TIME,
                       FOREIGN KEY (flight_number) REFERENCES flights(flight_number) )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS flight_names(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       flight_name VARCHAR(100) )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS airport_names(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       airport_name VARCHAR(100) )''')

        con.commit()  # Commit changes to the database
    except mysql.Error as e:
        print("Error:", e)


# Populate flight names table with default values if not already present
def populate_flight_names_table():
    try:
        # Retrieve existing flight names from the database
        cursor.execute("SELECT flight_name FROM flight_names")
        existing_flight_names = cursor.fetchall()
        existing_flight_names = [name[0] for name in existing_flight_names]

        # Define new flight names to be added
        new_flight_names = ['IndiGo', 'Air India', 'Vistara']

        # Iterate through new flight names and add them to the table if not already present
        for flight_name in new_flight_names:
            if flight_name not in existing_flight_names:
                # Insert new flight name into the table
                cursor.execute("INSERT INTO flight_names (flight_name) VALUES (%s)", (flight_name,))
                # Commit the transaction to save the changes
                con.commit()
    except mysql.Error as e:
        print("Error:", e)


def populate_airport_names_table():
    try:
        cursor.execute("SELECT airport_name FROM airport_names")
        existing_airport_names = cursor.fetchall()
        existing_airport_names = [name[0] for name in existing_airport_names]

        new_airport_names = ['Mumbai', 'Delhi', 'Kolkata']

        for airport_name in new_airport_names:
            if airport_name not in existing_airport_names:
                cursor.execute("INSERT INTO airport_names (airport_name) VALUES (%s)", (airport_name,))
                con.commit()
    except mysql.Error as e:
        print("Error:", e)


# Define the range of days for which flights will be generated
flight_days_range = 3

# Function to add flights to the database
def add_flights():
    try:
        # Check if flights already exist in the database
        cursor.execute("SELECT COUNT(*) FROM flights")
        count = cursor.fetchone()[0]

        if count > 0:
            return

        # Define flight data for different combinations of flights, airports, and timings
        flights_data = []
        airports = ['Mumbai', 'Delhi', 'Kolkata']
        today = datetime.date.today()

        for flight_number in range(101, 106):
            for origin in airports:
                for destination in airports:
                    if origin != destination:  # Exclude flights from a city to itself
                        for i in range(flight_days_range):
                            # Calculate the departure date
                            departure_date = today + datetime.timedelta(days=i)
                            
                            # Generate a random departure time
                            departure_hour = random.randint(0, 23)
                            departure_minute = random.choice(range(0, 59, 10))
                            departure_time = datetime.datetime(departure_date.year, departure_date.month, departure_date.day, departure_hour, departure_minute)
                            
                            # Generate a random duration for the flight (between 1 and 6 hours)
                            departure_to_arrival_duration = datetime.timedelta(hours=random.randint(1, 5))
                            
                            # Calculate the arrival time by adding the duration to the departure time
                            arrival_time = departure_time + departure_to_arrival_duration
                            
                            # If arrival time is after midnight, adjust it to the next day
                            if arrival_time.day != departure_date.day:
                                arrival_time = arrival_time.replace(day=departure_date.day + 1)
                            
                            # Ensure that departure time is before arrival time
                            while arrival_time <= departure_time:
                                departure_to_arrival_duration = datetime.timedelta(hours=random.randint(1, 6))
                                arrival_time = departure_time + departure_to_arrival_duration
                            
                            # Convert departure_time and arrival_time to string format
                            departure_time_str = departure_time.strftime('%H:%M:%S')
                            arrival_time_str = arrival_time.strftime('%H:%M:%S')
                            
                            # Generate a random number of available seats between 80 and 100
                            available_seats = random.randint(80, 100)
                            
                            # Generate a random cost for the flight ranging from 4000 to 7500
                            cost = random.choice(range(4000, 7501, 500))  # Ensure cost is in multiples of 500
                            
                            airline = ['IndiGo', 'Air India', 'Vistara'][flight_number % 3]

                            # Append flight data to the flights_data list
                            flights_data.append((flight_number, airline, origin, destination, departure_date, arrival_time_str, departure_time_str, available_seats, cost))

        # Insert flights data into the database
        cursor.executemany("INSERT INTO flights VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", flights_data)
        con.commit()
        print("Flights added successfully!")
    except mysql.Error as e:
        print("Error:", e)


# Function to display flight names
def display_flight_names():
    try:
        cursor.execute("SELECT * FROM flight_names")
        flight_names = cursor.fetchall()
        if not flight_names:
            print("No flight names available")
        else:
            print("List of Flight Names: ")
            for idx, flight_name in enumerate(flight_names, 1):
                print(f"{idx}. {flight_name[1]}")
                print("----------------------------")
    except mysql.Error as e:
        print("Error:", e)

# Function to display airport names
def display_airport_names():
    try:
        cursor.execute("SELECT * FROM airport_names")
        airport_names = cursor.fetchall()
        if not airport_names:
            print("No airport names available")
        else:
            print("List of Airport Names: ")
            for idx, airport_name in enumerate(airport_names, 1):
                print(f"{idx}. {airport_name[1]}")
                print("----------------------------")
    except mysql.Error as e:
        print("Error:", e)

# Function to search for flights based on origin and destination
def search_flights():
    origin = input("Enter Origin Airport: ")
    destination = input("Enter Destination Airport: ")

    try:
        cursor.execute("SELECT * FROM flights WHERE origin = %s AND destination = %s", (origin, destination))
        flights = cursor.fetchall()

        if not flights:
            print("No flights available for the given origin and destination.")
        else:
            print("Available Flights:")
            for flight in flights:
                print(f"Flight Number: {flight[0]}")
                print(f"Airline: {flight[1]}")
                print(f"Departure Date: {flight[4]}")
                print(f"Departure Time: {flight[5]}")
                print(f"Arrival Time: {flight[6]}")
                print(f"Available Seats: {flight[7]}")
                print("----------------------------")
    except mysql.Error as e:
        print("Error:", e)

# Function to book a flight
def book_flight():
    origin = input("Enter Origin Airport: ")
    destination = input("Enter Destination Airport: ")
    
    try:
        cursor.execute("SELECT * FROM flights WHERE origin = %s AND destination = %s", (origin, destination))
        flights = cursor.fetchall()

        if not flights:
            print("No flights available for the given origin and destination.")
            return

        print("Available Flights:")
        for i in range(len(flights)):
            flight = flights[i]
            print("Option " + str(i + 1) + ":")
            print("Airline: " + flight[1])
            print("Departure Date: " + str(flight[4]))
            print("Departure Time: " + str(flight[5]))
            print("Arrival Time: " + str(flight[6]))
            print("Available Seats: " + str(flight[7]))
            print("----------------------------")

        # Ask the user to select a flight option
        chosen_option = int(input("Enter the option number of the flight you want to book: "))
        try:
            if 1 <= chosen_option <= len(flights):
                chosen_flight = flights[chosen_option - 1]
                available_seats = chosen_flight[7]
                if available_seats > 0:
                    passenger_name = input("Enter Passenger Name: ")
                    try:
                        # Insert booking details with additional flight information
                        cursor.execute("INSERT INTO bookings (passenger_name, flight_number, airline, origin, destination, departure_date, departure_time, arrival_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                       (passenger_name, chosen_flight[0], chosen_flight[1], origin, destination, chosen_flight[4], chosen_flight[5], chosen_flight[6]))
                        cursor.execute("UPDATE flights SET available_seats = available_seats - 1 WHERE flight_number = %s",
                                       (chosen_flight[0],))
                        con.commit()
                        print("Flight Booked Successfully!")
                    except mysql.Error as e:
                        print("Error while booking flight:", e)
                else:
                    print("Sorry, no available seats for this flight.")
            else:
                print("Invalid option number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    except mysql.Error as e:
        print("Error while fetching data:", e)

# Function to display all bookings with flight details
def display_bookings():
    try:
        cursor.execute("SELECT * FROM bookings")
        bookings = cursor.fetchall()
        if not bookings:
            print("No bookings available")
        else:
            print("\nList of Bookings:\n")
            for booking in bookings:
                print("Booking ID:    ", booking[0])
                print("Passenger Name:", booking[1])
                print("Airline:       ", booking[3])
                print("Origin:        ", booking[4])
                print("Destination:   ", booking[5])
                print("Departure Date:", booking[6])
                print("Arrival Time:  ", booking[7])
                print("Departure Time:", booking[8])
                print("----------------------------")

    except mysql.Error as e:
        print("Error:", e)

# Function to cancel a booking
def cancel_booking():
    try:
        booking_id = input("Enter Booking ID: ")
        cursor.execute("SELECT flight_number FROM bookings WHERE id = %s", (booking_id,))
        flight_number = cursor.fetchone()[0]
        cursor.execute("DELETE FROM bookings WHERE id = %s", (booking_id,))
        cursor.execute("UPDATE flights SET available_seats = available_seats + 1 WHERE flight_number = %s",
                       (flight_number,))
        con.commit()
        print("Booking Cancelled Successfully!")
    except mysql.Error as e:
        print("Error:", e)

# Function to update passenger information
def update_passenger_info():
    booking_id = input("Enter Booking ID: ")
    old_passenger_name = input("Enter Old Passenger Name: ")
    new_passenger_name = input("Enter New Passenger Name: ")

    try:
        cursor.execute("UPDATE bookings SET passenger_name = %s WHERE id = %s AND passenger_name = %s",
                       (new_passenger_name, booking_id, old_passenger_name))
        con.commit()
        print("Passenger Information Updated Successfully!")
    except mysql.Error as e:
        print("Error:", e)


# Function to retrieve flight status
def retrieve_flight_status():
    flight_number = input("Enter Flight Number: ")
    try:
        cursor.execute("SELECT * FROM flights WHERE flight_number = %s", (flight_number,))
        flight = cursor.fetchone()
        if flight:
            print("Flight Status:")
            print(f"Airline: {flight[1]}")
            print(f"Origin: {flight[2]}")
            print(f"Destination: {flight[3]}")
            print(f"Departure Time: {flight[4]}")
            print(f"Arrival Time: {flight[5]}")
            print(f"Available Seats: {flight[6]}")
        else:
            print("Invalid flight number.")
    except mysql.Error as e:
        print("Error:", e)

# Function to list airports served
def list_airports_served():
    try:
        cursor.execute("SELECT DISTINCT origin FROM flights")
        origins = cursor.fetchall()
        cursor.execute("SELECT DISTINCT destination FROM flights")
        destinations = cursor.fetchall()

        if not origins and not destinations:
            print("No airports served")
        else:
            print("List of Airports Served:")
            print("Origins:")
            for origin in origins:
                print(origin[0])
            print("\nDestinations:")
            for destination in destinations:
                print(destination[0])
    except mysql.Error as e:
        print("Error:", e)

# Function to update flight details
def update_flight_details():
    flight_number = input("Enter Flight Number to update details: ")

    try:
        cursor.execute("SELECT * FROM flights WHERE flight_number = %s", (flight_number,))
        flight = cursor.fetchone()

        if not flight:
            print("Flight not found")
            return

        print("Existing Details:")
        print(f"Airline: {flight[1]}")
        print(f"Origin: {flight[2]}")
        print(f"Destination: {flight[3]}")
        print(f"Departure Time: {flight[4]}")
        print(f"Arrival Time: {flight[5]}")
        print(f"Available Seats: {flight[6]}")

        # Offer options to update details
        print("Update Options:")
        print("1. Airline")
        print("2. Origin")
        print("3. Destination")
        print("4. Departure Time")
        print("5. Arrival Time")
        print("6. Available Seats")

        update_choice = input("Enter your choice (1-6): ")

        if update_choice == '1':
            new_airline = input("Enter new Airline: ")
            cursor.execute("UPDATE flights SET airline = %s WHERE flight_number = %s", (new_airline, flight_number))
        elif update_choice == '2':
            new_origin = input("Enter new Origin: ")
            cursor.execute("UPDATE flights SET origin = %s WHERE flight_number = %s", (new_origin, flight_number))
        elif update_choice == '3':
            new_destination = input("Enter new Destination: ")
            cursor.execute("UPDATE flights SET destination = %s WHERE flight_number = %s", (new_destination, flight_number))
        elif update_choice == '4':
            new_departure_time = input("Enter new Departure Time (HH:MM:SS): ")
            cursor.execute("UPDATE flights SET departure_time = %s WHERE flight_number = %s", (new_departure_time, flight_number))
        elif update_choice == '5':
            new_arrival_time = input("Enter new Arrival Time (HH:MM:SS): ")
            cursor.execute("UPDATE flights SET arrival_time = %s WHERE flight_number = %s", (new_arrival_time, flight_number))
        elif update_choice == '6':
            new_available_seats = int(input("Enter new Available Seats: "))
            cursor.execute("UPDATE flights SET available_seats = %s WHERE flight_number = %s", (new_available_seats, flight_number))

        con.commit()
        print("Flight details updated successfully!")
    except mysql.Error as e:
        print("Error:", e)

# Function to generate reports
def generate_reports():
    print("Generate Reports:")
    print("1. Flights Report")
    print("2. Bookings Report")
    print("3. Exit Reports")

    report_choice = input("Enter your choice (1-3): ")

    if report_choice == '1':
        try:
            cursor.execute("SELECT * FROM flights")
            flights = cursor.fetchall()
            if not flights:
                print("No flights available")
            else:
                print("Flight Report: ")
                for flight in flights:
                    print(f"Flight Number: {flight[0]}")
                    print(f"Airline: {flight[1]}")
                    print(f"Origin: {flight[2]}")
                    print(f"Destination: {flight[3]}")
                    print(f"Departure Time: {flight[4]}")
                    print(f"Arrival Time: {flight[5]}")
                    print(f"Available Seats: {flight[6]}")
                    print("----------------------------")
        except mysql.Error as e:
            print("Error:", e)
    elif report_choice == '2':
        try:
            cursor.execute("SELECT * FROM bookings")
            bookings = cursor.fetchall()
            if not bookings:
                print("No bookings available")
            else:
                print("Bookings Report: ")
                for booking in bookings:
                    print(f"Booking ID: {booking[0]}")
                    print(f"Flight Number: {booking[1]}")
                    print(f"Passenger Name: {booking[2]}")
                    print("----------------------------")
        except mysql.Error as e:
            print("Error:", e)


def read_inserted_flights():
    try:
        cursor.execute("SELECT * FROM flights")
        flights = cursor.fetchall()
        if not flights:
            print("No flights available")
        else:
            print("Inserted Flights:")
            for flight in flights:
                print(f"Flight Number: {flight[0]}")
                print(f"Airline: {flight[1]}")
                print(f"Origin: {flight[2]}")
                print(f"Destination: {flight[3]}")
                print(f"Departure Date: {flight[4]}")
                print(f"Arrival Time: {flight[6]}")
                print(f"Departure Time: {flight[5]}")
                print(f"Available Seats: {flight[7]}")
                print(f"Cost: {flight[8]}")  # Include the cost of the flight
                print("----------------------------")
    except mysql.Error as e:
        print("Error:", e)



# Main function to execute the program
def main():
    create_tables()
    populate_flight_names_table()
    populate_airport_names_table()
    add_flights()
    while True:
        print('''
FLIGHT MANAGEMENT SYSTEM
1. Display Flight Names
2. Display Airport Names
3. Search Flights
4. Book Flight
5. Display Bookings
6. Cancel Booking
7. Retrieve Flight Status
8. Update Passenger Information
9. List Airports Served
10. Update Flight Details
11. Generate Reports
12. Read Inserted Flights
13. Exit
              ''')
        
        choice = input("\nEnter your choice (1-13): ")

        if choice == '1':
            display_flight_names()
        elif choice == '2':
            display_airport_names()
        elif choice == '3':
            search_flights()
        elif choice == '4':
            book_flight()
        elif choice == '5':
            display_bookings()
        elif choice == '6':
            cancel_booking()
        elif choice == '7':
            retrieve_flight_status()
        elif choice == '8':
            update_passenger_info()
        elif choice == '9':
            list_airports_served()
        elif choice == '10':
            update_flight_details()
        elif choice == '11':
            generate_reports()
        elif choice == '12':
            read_inserted_flights()
        elif choice == '13':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close database connection
if con.is_connected():
    cursor.close()
    con.close()