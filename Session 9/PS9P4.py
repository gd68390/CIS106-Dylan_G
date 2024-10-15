def fprice(miles):
    if miles >= 30:
        price = 12 * miles
    elif 29 >= miles >= 20:
        price = 10 * miles
    elif 19 >= miles >= 10:
        price = 8 * miles
    else:
        price = 5 * miles

    return price


s = 0

y = input("Would you like to calculate train fare prices? (Yes or No): ").capitalize()

while y == "Yes":

    name = input("What is your last name?: ")
    miles = float(input("How many miles are you from Downtown Chicago?: "))

    ticket = fprice(miles)

    s = s + ticket

    print()
    print(f"Train ticket price: ${ticket:.2f}")

    y = input("Would you like to calculate train fare prices again? (Yes or No): ").capitalize()

print()
print(f"Total price of all train tickets: ${s:.2f}")
    