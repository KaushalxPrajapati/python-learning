import pickle
stu={}
found = False
fin=open('Student.dat','rb')
try:
    print("Searching in File Stu.dat... ")
    while True:
        stu = pickle.load (fin)
        if stu['marks']>91:
            print (stu)
            found=True
except EOFError:
    if found == False:
        print("No such records found in the file")
    else:
        print ("Search successful.")
    fin.close()