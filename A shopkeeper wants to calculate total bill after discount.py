#A shopkeeper wants to calculate total bill after discount.
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

final_price = (lambda p, d: p - (p * d / 100))(price, discount)

print("Final price after discount =", final_price)
