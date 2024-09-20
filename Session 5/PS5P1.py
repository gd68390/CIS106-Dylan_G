#input

widgets = int(input("How many widgets do you have? :"))


#process

if widgets > 10000:
    price = 10
elif 10000 >= widgets >= 5000:
    price = 20
else:
    price = 30

extendedprice = widgets * price
tax = .07 * extendedprice
total = extendedprice + tax


#output

print(f"Extended Price: ${extendedprice:.2f}")
print("Tax: ${:.2f}".format(tax))
print(f"Total: ${total:.2f}")
