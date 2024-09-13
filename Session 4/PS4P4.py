#input

Name = input("Name of Appliance: ")
Cost = float(input("Cost of Appliance?: $"))


#process

if Cost <= 1000:
    WarrantyPrice = round((.05 * Cost),2)
else:
    WarrantyPrice = round((.1 * Cost),2)


#output

print("Name of Appliance:",Name)
print("Cost of Appliance: $",Cost)
print("Cost of Warranty: $",WarrantyPrice)
print("Total Cost: $",Cost + WarrantyPrice)

