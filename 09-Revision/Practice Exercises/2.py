# product_1 = float(input("Enter the price: "))
# product_2 = float(input("Enter the price: "))
# product_3 = float(input("Enter the price: "))

# # Find the Total Bill:
# total_bill = product_1 + product_2 + product_3
# print("Total Bill Amount is:", total_bill)

# # Find the Average Price:
# avg = total_bill / 3
# print("Average is: ", round(avg, 2))


print("-" * 100)

superhero_name = input("Enter a Superhero name: ")
print("s" in superhero_name)  # has a bug!
print("s" in superhero_name.lower()) # has no bug!
