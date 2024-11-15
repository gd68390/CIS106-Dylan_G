full_name = input("Enter your first and last name: ").title()

my_list = full_name.split()

while full_name == '' or len(my_list) != 2:

    print()
    full_name = input("Error. Please enter your first and last name: ").title()
    my_list = full_name.split()

print()
first_letter = full_name[:1]
f = my_list[1] + ", " + first_letter + "."
print(f)
        







    
