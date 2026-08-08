import mysql.connector as mysql

def create_db():
    mycon = mysql.connect(
        host="localhost",
        user="root",
        password="123456",
    )

    name = input("Enter database name: ")
    query = "create database if not exists " + name

    cur = mycon.cursor()
    cur.execute(query)
    print("Database created successfully !")


create_db()
