import mysql.connector as mysql

def connect():
    mycon=mysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="student"
    )
    if mycon.is_connected():
        print("Successfull")


    cur=mycon.cursor()
    cur.execute("select * from marksheet;")
    data=cur.fetchone()
    print(type(data))
    print("Total no. of rows retrieved :",cur.rowcount)

    for i in data:
        print(i)

    mycon.close()
