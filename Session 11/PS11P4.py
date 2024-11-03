def player(avg, name):
    global l
    l = len(name)
    print("Player Name:", "        ", "Batting Average:")
    for x in range(0,l,1):
        c = name[x]
        n = int((26-len(c)))
        print(name[x], f"{avg[x]:{n}.3f}")
    print()


def lookup(y,name,avg):
    if any(x == y for x in name) == True:
        x = name.index(y)
        print()
        print("Player Name:", "        ", "Batting Average:")
        c = name[x]
        n = int((26-len(c)))
        print(name[x],f"{avg[x]:{n}.3f}")
    print()

        


f = open("batting.txt", "r")

r = f.readline()

avg = []
name = []

while r != "":
    name.append(str(r).rstrip("\n"))
    a = float(f.readline())
    avg.append(a)
    r = f.readline()

f.close()

player(avg, name)

look = input("Would you like to find player batting averages? (Yes or No): ").capitalize()

while look == "Yes":

    print()
    y = str(input("Enter a player last name: ")).capitalize()

    lookup(y,name,avg)

    look = input("Would you like to find another player's batting averages? (Yes or No): ").capitalize()



   

