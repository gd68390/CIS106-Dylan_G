#input

BookQuantity = float(input("How many books are you ordering?: "))
BookCost = float(input("How much do each book cost?: $"))


#process

OrderTotal = round((BookQuantity * BookCost),2)

if OrderTotal < 50:
    Shipping = 25
else:
    Shipping = 0


#output

print("Order Subtotal: $",OrderTotal)
print("Shipping Cost: $",Shipping)
print("Order Total: $",OrderTotal + Shipping)