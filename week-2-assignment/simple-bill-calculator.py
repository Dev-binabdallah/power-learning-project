price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
total = price * float(quantity)

print(f"{quantity} items at {price:.2f} each is = {total:.2f}")
