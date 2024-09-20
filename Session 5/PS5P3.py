#input

cd = float(input("What is the principle amount of the CD?: $"))
maturity = float(input("How many years until the CD matures?: "))


#process

if cd > 100000 and maturity == 5:
    interest = .06
elif 50000 <= cd <= 100000 and maturity == 10:
    interest = .05
elif 50000 <= cd <= 100000 and maturity == 5:
    interest = .04
else:  
    interest = .02

fyinterest = interest * cd


#output

print(f"Principle: ${cd:.2f}")
print(f"Interest rate: {(interest*100):.2f}%")
print("First year interest: ${:.2f}".format(fyinterest))
