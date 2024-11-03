def highlow(name,score):
    l = len(name)
    hiscore = -1
    loscore = 1000
    for x in range(0,l,1):
        if float(score[x]) > float(hiscore):
            hiindex = x
            hiscore = score[x]

        if float(score[x]) < float(loscore):
            loindex = x
            loscore = score[x]

    print("Lowest student score: ", name[loindex], ":    ",loscore,"%") 
    print()
    print("Highest student score: ", name[hiindex], ":    ", hiscore, "%")


f = open("textpractice.txt", "r")

name = []
score = []

data = f.readline()

while data != "":
    
    name.append(str(data).rstrip("\n"))
    s = int(f.readline())
    score.append(s)
    data = f.readline()

f.close()

highlow(name,score)
