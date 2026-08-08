import pickle

fh=open("stud.dat","wb")
while True:
    name=input("enter student name:")
    age=int(input("enter age of the student:"))
    address=input("enter student's address:")
    student=[name,age,address]
    pickle.dump(student,fh)
    choice = input("Press Enter to continue or type anything else to exit: ")
    if choice:
         break
        
fh.close()    
        
