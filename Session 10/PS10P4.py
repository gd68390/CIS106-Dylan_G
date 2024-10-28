def avg(handi, norm):

    handi_avg = int(handi)/3
    norm_avg = int(norm)/3

    return handi_avg, norm_avg


name = input("What is your last name?: ").capitalize()
norm = int(input("What was your 3 game norm without handicap?: "))
handi = int(input("What was your 3 game norm with handicap?: "))

handi_avg, norm_avg = avg(handi, norm)

print("Bowler last name: ",name)
print("Average bowling score: ", norm_avg)
print("Average bowling score with handicap: ",handi_avg)

