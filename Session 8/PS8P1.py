def fextprice(qty,price):

    extprice = qty * price

    if extprice > 100000:
        discount = extprice * 0.1
    else:
        discount = 0

    newtotal = extprice - discount

    return newtotal



totaltotal = 0

a = input("Do you want to calculate extended price? (Yes or No): ")

while a == "Yes" or a == "yes":

    qty = int(input("How many units are there?: "))
    price = float(input("How much does each unit cost?: $"))

    total = fextprice(qty,price)

    totaltotal = totaltotal + total


    print("Quantity: ",qty)
    print("Price: $",price)
    print("Total: $",total)


    a = input("Would you like to continue to enter values into the program? (Yes or No): ")


print("Totals of all orders: $",totaltotal)






