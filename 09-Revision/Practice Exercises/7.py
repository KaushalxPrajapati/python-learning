roll_no = [101, 102, 103, 103, 102, 101, 104, 105]

# Method 1
temp_list = []  # Create an empty list to store unique elements
for num in roll_no:
    if num not in temp_list:
        temp_list.append(num)

roll_no = temp_list
print("Unique Roll Numbers: ", roll_no)

# Method 2
unique_roll_no = set(roll_no)
roll_no = list(unique_roll_no)
print("Unique Roll Numbers: ", roll_no)
