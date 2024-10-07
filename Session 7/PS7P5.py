x = open("PS7P5.txt","r")

students = 0

tuition = 0

name = x.readline().rstrip('\n')

while name != "":
    district = x.readline().rstrip('\n')
    credit = float(x.readline().rstrip('\n'))
    if district == "I":
        cost = 250 * credit
    else:
        cost = 500 * credit

    print("Student last name:    ",name)
    print("Credits taken:        ",credit)
    print("Tuition owed:        $",cost)

    students = students + 1
    tuition = tuition + cost

    name = x.readline().rstrip('\n')

print("Number of students:     ",students)
print("Total tuition owed:    $",tuition)


    