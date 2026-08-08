# This function counts the occurrences of the word "is" in the given message.

def is_count():
    L=message.split()
    c=0
    for i in L:
        if "is" in i:
            c=c+1
    print(c)

message="This is his book"
is_count()
