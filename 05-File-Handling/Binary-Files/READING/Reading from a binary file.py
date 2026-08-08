import pickle

f=open("file_name","rb")
try:
    while True:
        Data=pickle.load(f)
        print(Data)
                
except EOFError:
    f.close()
