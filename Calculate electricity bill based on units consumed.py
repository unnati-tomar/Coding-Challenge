# Function to calculate bill
def calculate_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (100 * 7) + (units - 200) * 10

# Input
units = int(input("Enter units consumed: "))

# Function call
bill = calculate_bill(units)

# Output
print("Total electricity bill = ₹", bill)
