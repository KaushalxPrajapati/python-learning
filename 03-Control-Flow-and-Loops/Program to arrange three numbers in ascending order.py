# Program to print numbers in ascending order

#-----Method 1-----
x=int(input("Enter the first no. : "))
y=int(input("Enter the second no. : "))
z=int(input("Enter the third no. : "))
if x>y and x>z:
  if y>z:
    print(z,'<',y,'<',x)
  else:
    print(y,'<',z,'<',x)
  
elif y>x and y>z:
  if x>z:
    print(z,'<',x,'<',y)
  else:
    print(x,'<',z,'<',y)

elif z>x and z>y:
  if x>y:
    print(y,'<',x,'<',z )
  else:
    print(x,'<',y,'<',z)



#-----Method 2-----
numbers = []
numbers.append(int(input("Enter the first number: ")))
numbers.append(int(input("Enter the second number: ")))
numbers.append(int(input("Enter the third number: ")))

# Sort the numbers
numbers.sort()

# Print the sorted numbers in the desired format
print(numbers[0], "<", numbers[1], "<", numbers[2])
