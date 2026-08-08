f=open("info1.txt","r")
ch=' '
L=["a","e","i","o","u"]
vcount=0
ccount=0
scount=0
ncount=0
while ch:
    ch=f.read(1)
    if ch.lower() in L:
        vcount+=1
    elif ch==" ":
        scount+=1
    elif ch=="\n":
        ncount+=1
    else:
        ccount+=1

print("No. of vowels are:", vcount)
print("No. of consonants are:", ccount)
print("No. of special characters are:", ncount)
print("No. of spaces are:", scount)
f.close()
