#Print all even numbers between 1 to N
# Input from user
n = int(input("Enter the value of N: "))

# Print even numbers
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
