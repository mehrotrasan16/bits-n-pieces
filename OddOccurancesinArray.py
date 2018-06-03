x = list(raw_input("#1 Enter a list of numbers,\n #2 The list should be of odd length,\n #3 All numbers in the list should have a duplicate in the list except one.\n List: "))
#x = [9,3,9,3,9,7,9]

flag = []

for i in x:
    if(i not in flag) :
        flag.append(i)
    else:
        flag.pop(flag.index(i))

print flag
