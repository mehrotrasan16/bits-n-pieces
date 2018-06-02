x = [9,3,9,3,9,7,9]

flag = []

for i in x:
    if(i not in flag) :
        flag.append(i)
    else:
        flag.pop(flag.index(i))

print flag
