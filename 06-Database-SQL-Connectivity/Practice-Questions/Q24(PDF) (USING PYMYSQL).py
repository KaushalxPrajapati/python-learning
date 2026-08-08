#USING PYMYSQL

import pymysql as ms

db = ms.connect(host="localhost",
                user="root", 
                password="123456", 
                database="school")
c = db.cursor()

#Function to create Database as per users choice
def c_database():
    try:
        dn = input("Enter Database Name=")
        c.execute("create database if not exists {}".format(dn))
        c.execute("use {}".format(dn))
        print("Database created successfully")
    except Exception as a:
        print("Database Error:", a)

#Function to Drop Database as per users choice
def d_database():
    try:
        dn = input("Enter Database Name to be dropped=")
        c.execute("drop database {}".format(dn))
        print("Database deleted successfully")
    except Exception as a:
        print("Database Drop Error:", a)

#Function to create Table
def c_table():
    try:
        c.execute('''create table if not exists students(
                     rollno int(3),
                     stname varchar(20))''')
        print("Table created successfully")
    except Exception as a:
        print("Create Table Error:", a)

#Function to Insert Data
def e_data():
    try:
        while True:
            rno=int(input("Enter student rollno="))
            name = input("Enter student name=")
            c.execute("insert into students values({},'{}');".format(rno,name))
            db.commit()
            choice=input("Do you want to add more record<y/n>=")
            if choice in "Nn":
                break
    except Exception as a:
        print("Insert Record Error:", a)

#Function to Display Data
def d_data():
    try:
        c.execute("select * from students")
        data = c.fetchall()
        for i in data:
            print(i)
    except Exception as a:
        print("Display Record Error:", a)

while True:
    print("\nMENU\n1. Create Database\n2. Drop Database\n3. Create Table\n4. Insert Record\n5. Display Entire Data\n6. Exit")
    choice=int(input("Enter your choice<1-6>="))
    if choice == 1:
        c_database()
    elif choice == 2:
        d_database()
    elif choice == 3:
        c_table()
    elif choice == 4:
        e_data()
    elif choice == 5:
        d_data()
    elif choice == 6:
        break
    else:
        print("Wrong option selected")
