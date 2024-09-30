a = input("Would you like to calculate employee gross pay for the week (Yes or No)?: ")

employees = 0
total = 0

while a == "Yes" or a == "yes":
    name = input("What is your last name?: ")
    hours = float(input("How many hours did you work this week?: "))
    rate = float(input("How much are you paid per hour?: "))

    if hours > 40:
        gross = (40 * rate) + ((hours - 40) * 1.5 * rate)
    else:
        gross = rate * hours


    print("Employee last name:", name)
    print(f"Gross pay: ${gross:.2f}")


    employees = employees + 1
    total = total + gross

    a = input("Would you like to continue to calculate employee gross pay for the week (Yes or No)?: ")

avg = total / employees
print("Number of employees:",employees)
print(f"Sum of all gross pay: ${total:.2f}")
print(f"Average pay: ${avg:.2f}")


