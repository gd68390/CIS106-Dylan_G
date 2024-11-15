line = input("Enter data points separated by commas: ")

line_2 = line.replace(' ','')

s = line_2.split(',')

l = len(s)

for x in range(0,l,1):

    print(s[x])
