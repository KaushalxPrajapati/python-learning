import pickle
def addplus2():
        stu={}
        found=False
        f=open('student.dat','rb+')
        try:
            while True:
                pos = f.tell () #Current position of file pointer
                stu = pickle.load(f)
                if stu['marks'] > 81:
                    stu['marks'] += 2
                    f.seek (pos)  
                    pickle.dump (stu, f)
                found=True
        except EOFError:
            if found == False:
                print("Sorry, no matching record found. ")
            else:
                print("Record(s) successfully updated. ")
        f.close()


#addplus2()

def read(): #Reading Updated Data !
    import pickle
    try:
        with open('student.dat','rb') as f:
            try:
                while True:
                    Data=pickle.load(f)
                    print(Data)
            except EOFError:
                    f.close()
    except Exception as e:
         print(e)

print("Updated results are...")
read()
