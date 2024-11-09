
#1.
integer = []
n = int(input("How many items will be in this list?: "))
for n in range(0,n,1):
   i = int(input("Enter an integer: "))
   integer.append(i)
print(integer)

#2.
integer.insert(1,99)
print(integer)

#3.
integer[1] = 100
print(integer)

#4.
number = [500,600,700,800,900]
print(number)
integer.extend(number)
print(integer)

#5.
integer.remove(800)
print(integer)

#6.
del integer[2]
print(integer)

#7.
grades = ["A","B","C","A","A","C"]

#8.
print(grades.count("A"))

#9.
print(grades.index("B"))

#10.
if any(x == "F" for x in grades) == True:
    print("Letter found")
else:
    print("Letter not found")

#11.
number.clear()
print(number)

#12.
del number
print(number)

#13.
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

#14.
players.sort()
print(players)

#15.
players2 = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print(players2)

#16.
players2.sort(reverse=True)
print(players)
print(players2)
