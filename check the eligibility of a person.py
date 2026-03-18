# check eligibility for a people using for loop
for i in range(n):
    age = int(input(f"Enter age of person {i+1}: "))
    
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
