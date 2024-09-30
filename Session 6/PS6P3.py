count = 0
a = input("Would you like to enter your exam scores (Yes or No)?: ")

while a == "yes" or a == "Yes":
    name = input("What is your last name?: ")
    e1 = float(input("What is your first exam score?: "))
    e2 = float(input("What is your second exam score?: "))
    avg = ((e1 + e2)/2)

    print("Last Name: ",name)
    print("Average exam score: ",avg)

    count = count + 1

    a = input("Would you like to enter another student into the program (Yes or No)?: ")

print("Number of students who entered data: ",count)
