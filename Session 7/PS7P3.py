x = open("PS7P3.txt","r")
total = 0

name = x.readline().rstrip('\n')

while name != "":
    salary = float(x.readline().rstrip('\n'))

    if salary >= 100000:
        bonus = .2 * salary
    elif salary >= 50000:
        bonus = .15 * salary
    else:
        bonus = .1 * salary

    print("Employee last name: ",name)
    print("Employee salary:     $",salary)
    print("Employee bonus:      $",bonus)

    total = total + bonus

    name = x.readline().rstrip('\n')

print("Sum of all bonuses   $",total)


