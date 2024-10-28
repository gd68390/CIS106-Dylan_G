def commission(sales):

    if float(sales) > 100000:
        commission = .10 * float(sales)
    else:
        commission = .05 * float(sales)

    target = 1.05 * sales

    return commission, target



name = input("What is your last name?: ").capitalize()
sales = float(input("How much were your sales this year?: $"))

commission, target = commission(sales)

print("Salesman last name: ",name)
print(f"Commission: ${commission:,.2f}")
print(f"Next year's target sales amount: ${target:,.2f}")
