def frate(code):
    if code == "L":
        rate = 25
    elif code == "A":
        rate = 30
    else:
        rate = 50

    return rate



net_gross = 0

y = input("Would you like to calculate your rate of pay? (Yes or No): ")

while y == "Yes" or y == "yes":

    name = input("What is your last name?: ").capitalize()
    code = input("What is your job code? (L, A, or J): ").capitalize()
    hours = float(input("How many hours did you work this week?: "))

    hourly = frate(code)

    if hours > 40:
        gross = (hourly * 40) + 1.5 * ((hours - 40) * hourly)
    else:
        gross = hourly * hours

    print("Employee last name: ",name)
    print(f"Gross week pay: ${gross:.2f}")

    net_gross = net_gross + gross

    y = input("Would you like to enter another employee's gross pay? (Yes or No): ")


print(f"Total employee gross pay: ${net_gross:.2f}")



