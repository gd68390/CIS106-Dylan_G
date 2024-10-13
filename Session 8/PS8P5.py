def ftuition(credit,code):
    if code == "I":
        hour = 250
    else:
        hour = 550

    rate = hour * credit

    return rate



t = 0

y = input("Would you like to calculate student's tuition costs? (Yes or No): ").capitalize()

while y == "Yes":
    
    name = input("What is your last name?: ").capitalize()
    credit = int(input("How many credit hours are you taking?: "))
    code = input("What is your district code? (I or O): ").capitalize()

    cost = ftuition(credit,code)

    print("Student last name: ",name)
    print(f"Tuition owed: ${cost:.2f}")

    t = t + cost

    y = input("Would you like to calculate another student's tuition costs? (Yes or No): ").capitalize()


print(f"Total of all tuition owed: ${t:.2f}")
