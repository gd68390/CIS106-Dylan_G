def f_msrp(make,model,code,msrp):

    if make == "Honda" and model == "Accord" and code == "N":
        p = .10
    elif make == "Toyota" and model == "Rav4" and code == "N":
        p = .15
    elif code == "Y":
        p = .30
    elif model != "Rav4" or model != "Accord" and code == "N":
        p = .05


    otdp = msrp - (msrp * p)
    sale = otdp + (.07 * otdp)

    return sale
    


s = 0
m = 0

y = input("Would you like to calculate potential savings on a new vehicle? (Yes or No): ").capitalize()

while y == "Yes":

    make = input("What make is the vehicle?: ").capitalize()
    model = input("What model is the vehicle?: ").capitalize()
    code = input("What is the electric vehicle code? (Y or N): ").capitalize()
    msrp = float(input("What is the MSRP of the vehicle?: $"))

    price = f_msrp(make,model,code,msrp)

    s = s + price
    m = m + msrp

    print()
    print(f"Price of the vehicle: ${price:,.2f}")
    print()
    y = input("Would you like to calculate potential savings on a new vehicle? (Yes or No): ").capitalize()
    print()


print(f"Total MSRP price of all vehicles: ${m:,.2f}")
print()
print(f"Total Out the door price of all vehicles: ${s:,.2f}")
print()
