f=open("info1.txt","r")
line=' '
while line:
    line=f.readline()
    for i in line.split():
        print(i,end="#")
    print()
    
f.close() 
