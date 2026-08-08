import mysql.connector as ms

db=ms.connect(
    host="localhost",
    user="root",
    password="123456",
    database="shop"
    )

cn=db.cursor()

def byCity():
    try:
        city=input("Enter city to search:")
        cn.execute("select * from customer where city='{}'".format(city))
        data=cn.fetchall()
        if data!=[]:
            cnt=0
            for i in data:
                cnt=cnt+1
                print('~'*50)
                print("Record:",cnt)
                print('~'*50)
                print("Customer ID:",i[0])
                print("Customer Name:",i[1])
                print("City:",i[2])
                print("Bill Amount:",i[3])
                print("Category:",i[4])
        else:
            print("No records found for city ", city)
    
    except Exception as e:
        print("Error",e)


def byBillAmt():
    try:
        ba=input("Enter the bill amount:")
        cn.execute("select * from customer where bill_amt={}".format(ba))
        data=cn.fetchall()
        if data!=[]:
            cnt=0
            for i in data:
                cnt=cnt+1
                print('~'*50)
                print("Record:",cnt)
                print('~'*50)
                print("Customer ID:",i[0])
                print("Customer Name:",i[1])
                print("City:",i[2])
                print("Bill Amount:",i[3])
                print("Category:",i[4])
        else:
            print("No records found for bill amount ", ba)
    
    except Exception as e:
        print("Error",e)


def byName():
    try:
        name=input("Enter the name:")
        cn.execute("select * from customer where cname='{}'".format(name))
        data=cn.fetchall()
        if data!=[]:
            cnt=0
            for i in data:
                cnt=cnt+1
                print('~'*50)
                print("Record:",cnt)
                print('~'*50)
                print("Customer ID:",i[0])
                print("Customer Name:",i[1])
                print("City:",i[2])
                print("Bill Amount:",i[3])
                print("Category:",i[4])
        else:
            print("No records found for ", name)
    
    except Exception as e:
        print("Error",e)


def byCat():
    try:
        cat=input("Enter the cat:")
        cn.execute("select * from customer where cat='{}'".format(cat))
        data=cn.fetchall()
        if data!=[]:
            cnt=0
            for i in data:
                cnt=cnt+1
                print('~'*50)
                print("Record:",cnt)
                print('~'*50)
                print("Customer ID:",i[0])
                print("Customer Name:",i[1])
                print("City:",i[2])
                print("Bill Amount:",i[3])
                print("Category:",i[4])
        else:
            print("No records found for category ", cat)
    
    except Exception as e:
        print("Error",e)


while True:
    print('''
MENU
1.Display customer details by city
2.Display customer details by bill amount
3.Display customer details by name
4.Display customer details by category
5.Exit
''')
    ch=int(input("Enter your choice<1-4>="))
    if ch==1:
        byCity()
    elif ch==2:
        byBillAmt()
    elif ch==3:
        byName()
    elif ch==4:
        byCat()
    elif ch==5:
        break
    else:
        print("Wrong option selected")
