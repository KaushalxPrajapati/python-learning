n=int(input("Enter the number : "))

fact=1
for i in range (n,0,-1):
  fact=fact*i
  
print("Factorial of",str(n),"is :",fact)
