# Input from user
price = float(input("Enter the price: "))
discount = float(input("Enter discount percentage: "))

# Calculate discount amount
discount_amount = (price * discount) / 100

# Final price
final_price = price - discount_amount

# Output
print("Final price after discount =", final_price)
