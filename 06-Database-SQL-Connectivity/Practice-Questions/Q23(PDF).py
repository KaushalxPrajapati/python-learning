import mysql.connector

# Function to create a MySQL connection
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="school"
        )
    return connection


# Function to create a database
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS school")
    cursor.close()


# Function to create a table
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("USE school")

    table_query = '''
    CREATE TABLE IF NOT EXISTS student (
        ROLLNO INT,
        STNAME VARCHAR(10)
    ) '''
    cursor.execute(table_query)
    connection.commit()
    cursor.close()


# Function to insert records into the table
def insert_records(connection, records):
    cursor = connection.cursor()
    cursor.execute("USE school")

    insert_query = "INSERT INTO student (ROLLNO, STNAME) VALUES (%s, %s)"
    cursor.executemany(insert_query, records)

    connection.commit()
    cursor.close()


# Function to display the contents of the table
def display_records(connection):
    cursor = connection.cursor()
    cursor.execute("USE school")

    select_query = "SELECT * FROM student"
    cursor.execute(select_query)

    records = cursor.fetchall()
    for record in records:
        print("ROLLNO:", record[0], "STNAME:", record[1])

    cursor.close()


# Main program
if __name__ == "__main__":
    # Create a connection
    connection = create_connection()

    # Create the 'school' database
    create_database(connection)

    # Create the 'student' table
    create_table(connection)

    # Insert records into the table
    records_to_insert = [(1, 'John'), (2, 'Jane')]
    insert_records(connection, records_to_insert)

    # Display the contents of the 'student' table
    display_records(connection)

    # Close the connection
    connection.close()
