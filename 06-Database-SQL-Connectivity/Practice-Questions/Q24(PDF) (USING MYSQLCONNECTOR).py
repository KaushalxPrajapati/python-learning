import mysql.connector as ms

db = ms.connect(
    host="localhost",
    user="root",
    password="123456",
    database='school')

cn = db.cursor()

def insert_rec():
    try:
        while True:
            rn = int(input("Enter roll number: "))
            sname = input("Enter name: ")
            marks = float(input("Enter marks: "))
            gr = input("Enter grade: ")

            cn.execute("INSERT INTO students VALUES({}, '{}', {}, '{}')".format(rn, sname, marks, gr))
            db.commit()
            ch = input("Want more records? Press (N/n) to stop entry: ")
            if ch in 'Nn':
                break
    except Exception as e:
        print("Error:", e)

def update_rec():
    try:
        rn = int(input("Enter roll number to update: "))
        marks = float(input("Enter new marks: "))
        gr = input("Enter Grade: ")
        cn.execute("update students set marks={}, gr='{}' WHERE rn={}".format(marks, gr, rn))
        db.commit()
    except Exception as e:
        print("Error:", e)

def delete_rec():
    try:
        rn = int(input("Enter roll number to delete: "))
        cn.execute("DELETE FROM students WHERE rn={}".format(rn))
        db.commit()
    except Exception as e:
        print("Error:", e)

def view_rec():
    try:
        cn.execute("SELECT * FROM students")
        data = cn.fetchall()
        for i in data:
            print(i)
    except Exception as e:
        print("Error:", e)

while True:
    print("\nMENU\n1. Insert Record\n2. Update Record \n3. Delete Record\n4. Display Record \n5. Exit")
    ch = int(input("Enter your choice <1-5>: "))
    if ch == 1:
        insert_rec()
    elif ch == 2:
        update_rec()
    elif ch == 3:
        delete_rec()
    elif ch == 4:
        view_rec()
    elif ch == 5:
        break
    else:
        print("Wrong option selected")


        
