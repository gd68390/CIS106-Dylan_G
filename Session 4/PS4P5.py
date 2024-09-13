#input

LastName = input("What is your last name?: ")
Dependents = int(input("How many dependents do you have?: "))
GrossIncome = float(input("What is your gross income?: $"))


#process

AGI = round((GrossIncome - (Dependents * 12000)),2)

if AGI > 0:
    TaxRate = .10
    if AGI > 50000:
        TaxRate = .20
    else:
        pass

if AGI > 0:
    IncomeTax = round((TaxRate * AGI),2)
else:
    IncomeTax = 100


#output

print("Last Name: ",LastName)
print("Dependents: ",Dependents)
print("Gross Income: $",GrossIncome)
print("Adjusted Gross Income: $",AGI)
print("Income Tax: $",IncomeTax)





