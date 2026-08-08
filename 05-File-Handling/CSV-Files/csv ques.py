from csv import reader, writer

# Display the current data in a CSV file named "top5.csv"
def display_data():
    # Open the file in read mode
    with open("top5.csv", "r") as file:
        # Read the CSV file
        csv_reader = reader(file)
        # Convert the data into a list
        data = list(csv_reader)
        # Display each row of data
        for row in data:
            print(row)

# Add a new row to the "top5.csv" file
def add_new_row(sno, batsman, team, runs, highest):
    # Open the file in append mode
    with open("top5.csv", "a", newline='') as file:
        # Create a CSV writer object
        csv_writer = writer(file)
        # Write a new row with the provided information
        csv_writer.writerow([sno, batsman, team, runs, highest])

# Display the current data in the CSV file
display_data()

# Add a new row with specific information
add_new_row(6, "NewPlayer", "NewTeam", 180, 100)

# Display the updated data after adding the new row
print("\nUpdated Data:")
display_data()
