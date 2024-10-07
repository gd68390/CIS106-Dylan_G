f = open("PS7P4.txt", "r")

c = 0.0
total = 0.0

item = str(f.readline().rstrip('\n'))

while item !="":
    qty = float(f.readline())
    price = float(f.readline())

    ep = qty * price
    total = total + ep

    c = c + 1

    print("Item is:                  ", item)
    print("Quantity is:              ", qty)
    print("Price is:                 $", price)
    print("Extended price is:        $", ep)

    item = str(f.readline().rstrip('\n'))


print("Total extended price is:  $", total)
print("Number of orders is:      ", c)

avg = total / c

print("Average order is:         $", avg)
