def fsquare(l,w,h):
    sqft = 2*(w*l) + 2*(h*l) + 2*(w*h)
    
    gal_sqft = sqft / 50

    return gal_sqft


c = 0

y = input("Would you like to calculate gallons of paint needed to paint a room? (Y or N): ").capitalize()

while y == "Y":
    l = float(input("What is the length of the room? (FT): "))
    w = float(input("What is the width of the room? (FT): "))
    h = float(input("What is the heigth of the room? (FT): "))

    paint = fsquare(l,w,h)

    print(f"Gallons of paint needed: {paint:.2f} GAL")

    c = c + 1

    y = input("Would you like to calculate gallons of paint needed to paint a room again? (Y or N): ").capitalize()

print("Total calculations made: ",c)
