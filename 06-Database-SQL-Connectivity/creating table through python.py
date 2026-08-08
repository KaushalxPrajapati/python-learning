import mysql.connector as mysql

mycon=mysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="shop"
    )

query='''create table if not exists customer(cid int, cname varchar(20),
city varchar(20),
bill_amt int,
cat varchar(20)
)'''

cur=mycon.cursor()
cur.execute(query)
print("Table created successfully !")

