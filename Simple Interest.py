 #Create a function to calculate simple interest
def simple_interest():
    while True:
        p = float(input("Enter Principal (P): "))
        r = float(input("Enter Rate (R): "))
        t = float(input("Enter Time (T): "))
        
        si = (p * r * t) / 100
        print("Simple Interest =", si)
        
        choice = input("Do you want to calculate again? (yes/no): ")
        if choice.lower() != 'yes':
            break

# Function call
simple_interest()
