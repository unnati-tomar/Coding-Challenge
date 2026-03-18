# Calculate electricity bill based on units consumed
units = int(input("Enter electricity units consumed: "))
bill = 0

for i in range(1, units + 1):
    if i <= 100:
        bill += 1.5
    elif i <= 200:
        bill += 2.5
    else:
        bill += 4

print("Total Electricity Bill = ₹", bill)
