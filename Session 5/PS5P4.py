#input

tickets = int(input("How many concert tickets do you have?: "))


#process

if tickets >= 25:
    price = 50
elif 10 <= tickets <= 24:
    price = 60
elif 5 <= tickets <= 9:
    price = 70
else:
    price = 75

total = tickets * price


#output
print("Number of tickets:",tickets)
print("Price per ticket: $",price)
print("Total cost: $",total)