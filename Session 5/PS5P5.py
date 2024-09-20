#input

name = input("What is your last name?: ")
salary = float(input("What is your salary?: $"))
level = float(input("What is your job level?: "))


#process

if level >= 10:
    rate = .25
elif 5 <= level <= 9:
    rate = .2
else:
    rate = .1

bonus = rate * salary


#output

print("Employee last name:",name)
print(f"Bonus: ${bonus:.2f}")