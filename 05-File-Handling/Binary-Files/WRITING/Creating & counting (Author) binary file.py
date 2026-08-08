import pickle

def createfile():
        fobj=open("Book.dat","wb+")
        ch="y"
        while ch=="y":
                BookNo=int(input("Enter Book Number: "))
                Book_name=input("Enter book Name")
                Author = input("Enter Author name: ")
                Price = int(input("Price of book: "))
                rec=[BookNo, Book_name ,Author,Price] 
                pickle.dump(rec, fobj)
                ch=input("want to add more press y or n to exit")
        fobj.close()

#createfile()


def count(Author):
    try:
        fobj = open("Book.dat", "rb")
        num = 0
        while True:
            try:
                rec = pickle.load(fobj)
                if Author.lower() == rec[2].lower():
                    num += 1

            except EOFError:
                    break
        fobj.close()
        return num

    except FileNotFoundError:
        print("File not found.")
        return 0

Author=input("Enter the name of the author to search")
print('''No. of book found by''', '"' + Author + '"', '''name is:''', count(Author))
