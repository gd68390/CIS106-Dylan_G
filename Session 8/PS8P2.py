def fbat(hit,bat):

    batavg = hit / bat

    return batavg



p = 0

y = input("Would you like to compute player batting averages? (Yes or No): ")

while y == "Yes" or y == "yes":

    name = input("What is the player's last name?: ").capitalize()
    hit = int(input("How many hits does the player have?: "))
    bat = int(input("How many at-bats does the player have?: "))

    batting = fbat(hit,bat)

    p = p + 1

    print("Player last name: ",name)
    print(f"Batting average: {batting:.3f}")

    y = input("Would you like to compute another player's batting average? (Yes or No): ")


print("Total players entered into program: ",p)


