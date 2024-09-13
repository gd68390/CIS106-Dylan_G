#input

ItemQuantity = float(input("Enter Item Quantity: "))


#process

if ItemQuantity >= 1000:
    UnitPrice = 3
else:
    UnitPrice = 5

ExtendedPrice = ItemQuantity * UnitPrice

Tax = round((.07 * ExtendedPrice),2)

TotalPrice = ExtendedPrice + Tax


#output

print("Item Quantity:",ItemQuantity)
print("Unit Price: $",UnitPrice)
print("Extended Price: $",ExtendedPrice)
print("Taxes: $",Tax)
print("Total: $",TotalPrice)