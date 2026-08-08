import mysql.connector as mysql

mycon=mysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="student"
    )

cur=mycon.cursor()
cur.execute("select * from marksheet;")
data=cur.fetchall()
count=cur.rowcount
print("Total no. of rows retrieved :",count)

print("________________________________")


for i in data:
    print("SNO:", i[0])
    print("SNAME:", i[1])
    print("ENGLISH:", i[2])
    print("PHYSICS:", i[3])
    print("CHEMISTRY:", i[4])
    print("MATHS:", i[5])
    print("CS:", i[6])
    print("TOTAL:", i[7])
    print("________________________________")

mycon.close()


