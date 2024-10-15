def fcast(month,sales):
    forecast = sales * (1 + p)

    return forecast


c = 0

y = input("Would you like to calculate sales forecast? (Y or N): ").capitalize()

while y == "Y":

    name = input("What is your last name?: ")
    month = int(input("What is the upcoming month? (1 - 12):"))
    
    if 1 <= month <= 3:
        p = .10
    elif 4 <= month <= 6:
        p = .15
    elif 7 <= month <= 9:
        p = .20
    else:
        p = .25
        
    sales = float(input("How much did make in sales this month?: $"))

    mforcast = fcast(month,sales)

    print(f"Next month's sales: ${mforcast:.2f}")

    c = c + 1
    
    y = input("Would you like to calculate another sale forecast? (Y or N): ").capitalize()

print("Total forecast entries: ",c)


