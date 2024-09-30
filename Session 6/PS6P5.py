a = input("Would you like to calculate discounts for items (Yes or No)?: ")
sale = 0

while a == "Yes" or a == "yes":
    qty = int(input("How many items are there?: " ))
    price = float(input("How much is each item?: $"))
    
    ext = qty * price

    if ext > 10000:
        discount = .25 * ext
    else:
        discount = .10 * ext

    print(f"Extended price: ${ext:.2f}")
    print(f"Discount amount: ${discount:.2f}")
    print(f"Total price: ${(ext-discount):.2f}")

    sale = sale + discount

    a = input("Would you like to countinue to calculate discounts for items (Yes or No)?: ")

print(f"Sum of all the discounts: ${sale:.2f}")


