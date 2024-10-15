def f_value(county,value):
    if county == "Cook":
        p = .90
    elif county == "Dupage":
        p = .80
    elif county == "Mchenry":
        p = .75
    elif county == "Kane":
        p = .60
    else:
        p = .70

    avalue = value * p

    return avalue




mv = 0
av = 0

y = input("Would you like to calculate assessed market value of a home? (Yes or No): ").capitalize()

while y == "Yes":

    county = input("What county is the home located in?: ").capitalize()
    value = float(input("What is the market value of the home?: $"))

    home_value = f_value(county,value)

    mv = mv + value
    av = av + home_value

    print()
    print(f"Assessed home value: ${home_value:,.2f}")
    print()

    y = input("Would you like to calculate assessed market value of a home again? (Yes or No): ").capitalize()

print()
print(f"Market value of all homes: ${mv:,.2f}")
print()
print(f"Assessed value of all homes: ${av:,.2f}")


