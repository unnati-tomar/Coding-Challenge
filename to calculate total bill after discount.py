# to calculate total bill after discount.
# Input from user
price = float(input("Enter the price: "))
discount = float(input("Enter discount percentage: "))

# Direct formula
final_price = price * (1 - discount / 100)

# Output
print("Final price after discount =", final_price)
Output
Enter the price: 677
Enter discount percentage: 15
Final price after discount = 575.4499999999999
