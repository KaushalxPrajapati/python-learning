def ABLINES():
    f=open("LINES.txt")
    list=f.readlines()
    for i in list:
        if i[0]=='A' or i[0]=='B' :
            print(i, end="" )
    f.close()

ABLINES()
