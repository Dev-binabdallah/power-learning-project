amount = float(input("How much money do you have: "))
number_of_books = int(input("How many books do you want: "))
price_per_book = 250
total_cost = float(number_of_books * price_per_book)
if amount >= total_cost:
    print("You can afford all the books.")
else:
    print(f"Not enought! You need {total_cost - amount:.2f} to buy the {number_of_books} book(s).")