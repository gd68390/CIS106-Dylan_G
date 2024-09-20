#input

partnumber = int(input("What is the part number?:" ))
quantity = float(input("How many parts do you have?: "))


#process

if partnumber == 10 or partnumber == 55:
    cost = 1.00
elif partnumber == 99:
    cost = 2.00
elif partnumber == 80 or partnumber == 70:
    cost = 3.00
else:
    pass

totalcost = quantity * cost


#output

print("Part Number: ",partnumber)
print("Cost Per Unit: ${:.2f}".format(cost))
print(f"Total Cost: ${totalcost:.2f}")