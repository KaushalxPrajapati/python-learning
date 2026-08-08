#This is a MODULE, which reads data from any BINARY FILE if provided JUST Name !

import pickle
def read():
    name=input("Enter file name:")
    name=name+".dat"
    with open(name, 'rb') as f:
        try:
            while True:
                Data=pickle.load(f)
                print(Data)
                
        except EOFError:
                f.close()

read()
