 #Calculate electricity bill based on units consumed.
# Input from user
units = int(input("Enter electricity units consumed: "))

# Calculate bill
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# Output
print("Total electricity bill = ₹", bill)
