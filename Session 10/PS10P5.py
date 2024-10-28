def total(qty,price):

    global total 
   
    total = qty * price

    global tax
    
    tax =.07 * total
   


qty = int(input("How many items are there?: "))
price = float(input("How much is each item?: $"))

total(qty,price)

print(f"Subtotal: ${total:,.2f}")
print(f"Total tax: ${tax:,.2f}")