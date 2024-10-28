def favg(e1,e2,e3):

    total = e1 + e2 + e3
    avg = (e1 + e2 + e3)/3

    return total, avg


name = input("What is your last name?: ").capitalize()
e1 = float(input("How many points did you get on your first exam?: "))
e2 = float(input("How many points did you get on your second exam?: "))
e3 = float(input("How many points did you get on your third exam?: "))

total, avg = favg(e1,e2,e3)

print("Student last name: ",name)
print("Total exam points earned: ",total)
print(f"Average points earned from exams: {avg:.2f}")