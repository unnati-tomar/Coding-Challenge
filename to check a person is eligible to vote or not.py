#to check a person is eligible to vote or not
age = int(input("Enter your age: "))

result = {True: "Eligible to vote", False: "Not eligible to vote"}

print(result[age >= 18])
Output
Enter your age: 67
Eligible to vote
