import mysql.connector as mysql

def fun1():
    mycon=mysql.connect(
    host="localhost",
    user="root",
    password="123456")
    
    cur=mycon.cursor()
    cur.execute("create database if not exists abcschool")

def fun2():
    mycon=mysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="abcschool"
    )
    cur=mycon.cursor()
    d2="create table if not exists student( name varchar(12), rollno int, Class int )"
    cur.execute(d2)

    d3='''insert into student value('Akash',2,12)'''
    cur.execute(d3)
    mycon.commit()
    print("Data Inserted Successfully!")
    mycon.close()
    

if __name__=="__main__":
    fun1()
    fun2()

