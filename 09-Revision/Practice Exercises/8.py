employee_record = [(101, "Alice", 50000), (102, "Bob", 65000), (103, "Charlie", 45000)]
emp_id = int(input("Enter Employee ID: "))

# Method 1 (using in operator)
for record in employee_record:
    if emp_id in record:
        print("Result found:", record)


# Method 2 (using the employee_id position directly)
for record in employee_record:
    if record[0] == emp_id:
        print("Result found:", record)


# Method 3 (using .index() method)
for record in employee_record:
    try:
        position = record.index(emp_id)
        print("Result found:", record)
        break
    except ValueError:
        continue
