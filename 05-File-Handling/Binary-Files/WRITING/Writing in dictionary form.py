def writedict():
        import pickle
        f=open("student.dat", 'ab')
        stu={}
        choice='y'
        while choice=='y':
                name = input("enter name")
                rollno= int(input("enter roll no. "))
                marks=int(input("enter marks "))
                stu={"name": name,"roll no" : rollno,"marks":marks}
                pickle.dump(stu,f)
                choice=input(" y or n")
        f.close()

#writedict()
        
import readbinary as r
r.read()
	
		

	
	
	
