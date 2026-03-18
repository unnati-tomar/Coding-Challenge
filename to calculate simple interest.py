 #Create a function to calculate simple interest.
# Function to calculate simple interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

# Input from user
p = float(input("Enter Principal (P): "))
r = float(input("Enter Rate of Interest (R): "))
t = float(input("Enter Time (T): "))

# Function call
result = simple_interest(p, r, t)

# Output
print("Simple Interest =", result)
Enter Principal (P): 34
Enter Rate of Interest (R): 25
Enter Time (T): 25
Simple Interest = 212.5

