string = input('Enter a line of text: ')
width = int(input('How many characters would you like printed per line? :'))
lines = int(input('How many lines would you like printed out?: '))
direction = input("Which direction would you like the text to go?: (Left or Right)").capitalize()

length = len(string)
array = list(string)
array.insert(length,' ')
shift = 0

for x in range(0,lines,1):

    if lines > length and (shift - 1) == length or (shift + 1) == (-length):
                
        shift = 0

        n = int((width/length) + 1)
        array_2 = (array[-shift:] + array[:-shift])
        array_3 = n * array_2
        line_2 = ''.join(array_3)

        print(line_2[0:width])
            

    else:

        n = int((width/length) + 1)
        array_2 = (array[-shift:] + array[:-shift])
        array_3 = n * array_2
        line_2 = ''.join(array_3)

        print(line_2[0:width])
  

    if direction == 'Right':
        shift = shift + 1

    else:
        shift = shift - 1
