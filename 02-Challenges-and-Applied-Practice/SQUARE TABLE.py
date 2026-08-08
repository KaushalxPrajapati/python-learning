# This program generates "SQUARE TABLE" within a specified range

def tables_sqr():
  start=int(input("Enter starting no. "))
  end=int(input("Enter ending no. "))
  for i in range(start,end+1):
    print(str(i)+'²','=',i*i)

while True:
  tables_sqr()
  choice = input("Press Enter to continue or type anything else to exit: ") # If the choice is not an empty string ( means user typed something)
  if choice != "": 
    break   # Exit the loop, as the user want to end the program.