#Input
Make = input("Enter Make of Vehicle: ")
Model = input("Enter Model of Vehicle: ")
MSRP = float(input("Enter MSRP of Vehicle: "))
Discount = float(input("Enter Discount Percentage: "))

#Process
DiscountAmount = round((MSRP * (Discount/100)),2)
DiscountPrice = round((MSRP - DiscountAmount),2)

#Output
print("Make: ",Make)
print("Model: ",Model)
print("MSRP: $",MSRP)
print("Discount Percentage: ",Discount,"%")
print("Amount Off Vehicle: $",DiscountAmount)
print("Discounted Price of Vehicle: $",DiscountPrice)