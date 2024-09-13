#input

Item = input("Do you have Item A or B?: ")
ItemQuantity = float(input("How many items do you have?: "))


#process

if Item == "A" or Item == "a":
    UnitPrice = 10
else:
    UnitPrice = 20

ExtendedPrice = ItemQuantity * UnitPrice   


#output

print("Item: A") if Item == "A" or Item == "a" else print("Item: B")
print("Unit Price: $",UnitPrice)
print("Extended Price: $",ExtendedPrice)