import mysql.connector as ms

db=ms.connect(
    host="localhost",
    user="root",
    password="123456",
    database="shop"
    )

cn=db.cursor()

def insert_rec():
    try:
        while True:
            cid=int(input("Enter customer id: "))
            cname=input("Enter name: ")
            city=input("Enter city: ")
            bill_amt=float(input("Enter bill amount: "))
            cat=input("Enter category: ")
            cn.execute("insert into customer values({},'{}','{}',{},'{}')".format(cid,cname,city,bill_amt,cat))
            db.commit()
            ch=input("Want more records? Press (N/n) to stop entry: ")
            if ch in 'Nn':
                break
            
    except Exception as e:
        print("Error", e)


def update_rec():
    try:
        cid = int(input("Enter customer id to update: "))
        cn.execute("SELECT * FROM customer")
        data = cn.fetchall()
        record_found = False

        for i in data:
            ci = i[0]
            cna = i[1]
            ct = i[2]
            b = i[3]
            c = i[4]

            if cid == ci:
                record_found = True

                ch_cname = input("Want to update Name, Press 'Y': ")
                if ch_cname.lower() == 'y':
                    cname = input("Enter new name: ")
                else:
                    cname = cna

                ch_city = input("Want to update city, Press 'Y': ")
                if ch_city.lower() == 'y':
                    city = input("Enter new city: ")
                else:
                    city = ct

                ch = input("Want to update bill amount, Press 'Y': ")
                if ch.lower() == 'y':
                    bill_amt = float(input("Enter new bill amount: "))
                else:
                    bill_amt = b

                ch_cat = input("Want to update Category, Press 'Y': ")
                if ch_cat.lower() == 'y':
                    cat = input("Enter new category: ")
                else:
                    cat = c
                    
                cn.execute('''update customer set cname='{}', city='{}', bill_amt={}, cat='{}' 
                           where cid={} '''.format(cname, city, bill_amt, cat, cid))
                db.commit()
                print("Data Updated Successfully...")
                break  # Break the loop once the record is updated

        if not record_found:
            print("Record Not Found...")

    except Exception as e:
        print("Error", e)


def delete_rec():
    try:
        cid=int(input("Enter customer id to delete : "))
        cn.execute("delete from customer where cid={}".format(cid))
        db.commit()
        print("Record Deleted...")
        
    except Exception as e:
        print("Error",e)
        
def view_rec():
    try:
        cn.execute("select * from customer")
        data=cn.fetchall()
        cnt=0
        for i in data:
            cnt=cnt+1
            print("Record:",cnt)
            print('~'*50)
            print("Customer ID:",i[0])
            print("Customer Name:",i[1])    
            print("City:",i[2])
            print("Bill Amount:",i[3])
            print("Category:",i[4])
            print('~'*50)
            
    except Exception as e:
        print("Error",e)
    

               
while True:
    print("\nMENU\n1. Insert Record\n2. Update Record \n3. Delete Record\n4. Display Record \n5. Exit")
    ch=int(input("Enter your choice<1-4>="))
    print()
    if ch==1:
        insert_rec()
    elif ch==2:
        update_rec()
    elif ch==3:
        delete_rec()
    elif ch==4:
        view_rec()
    elif ch==5:
        break
    else:
        print("Wrong option selected")
