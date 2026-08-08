import mysql.connector as mysql

mycon=mysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="student"
    )
if mycon.is_connected():
    print("Connection is Successfull")
