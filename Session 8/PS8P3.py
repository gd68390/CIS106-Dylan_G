def fmpg(miles,gal):

    if gal == 0:
        mpg = 0
    else:
        mpg = miles / gal

    return mpg



e = 0

y = input("Would you like to calculate fuel economy? (Yes or No):").capitalize()

while y == "Yes":

    destination = input("What place was the destination?: ").capitalize()
    miles = float(input("How many miles did you travel for this trip?: "))
    gal = float(input("How many gallons of gasoline was used to travel on this trip?: "))

    fuel_economy = fmpg(miles,gal)

    print("Destination: ",destination)
    print("Miles travelled: ",miles)
    print("Fuel economy: ",fuel_economy,"MPG")

    e = e + 1

    y = input("Would you like to add another trip into the program? (Yes or No): ").capitalize()


print("Trips made: ",e)