student=[]
choice = 'y'
while choice == 'y':
    dict = {}
    dict["Name"] = input("ENTER NAME: ")
    dict["Class"] = int(input("ENTER CLASS: "))
    dict["Roll"] = int(input("ENTER ROLL NO.: "))
    student.append(dict)
    choice = input("Press y to continue or n to exit: ")
    

for i in student:
    print(i)