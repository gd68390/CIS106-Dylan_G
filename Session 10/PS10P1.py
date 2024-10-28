def function(rate, price, qty):

    discount = price * qty - (price * qty * rate)
    amount = price * rate * qty

    return discount, amount



rate = float(input("What is the discount rate?"))
price = float(input("What is the price of each item?: $"))
qty = int(input("How many items is there?: "))

discount, amount = function(rate, price, qty)

print("Quantity of items: ",qty)
print(f"Price of each item: ${price:,.2f}")
print(f"Discounted price: ${discount:,.2f}")
print(f"Discount amount: ${amount:,.2f}")

