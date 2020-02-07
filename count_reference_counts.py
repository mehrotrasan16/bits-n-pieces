## Problem Statement: WAP that counts the number of references present
## in the given test of a paper

import os
os.chdir("D:\\User\\tmp\\")
f = open("Paper Test", mode='r+', encoding="utf8")
f.seek(0)
d = {}
d[0] = "Test Ref"
#init d

for num in range(1,31):
    print(num)
    f.seek(0)
    for line in f:
	#print(line)
	#print("["+str(num)+"]")
	#print(line.find("["+str(num)+"]"))
        if line.find("["+str(num)+"]") > 0 :
            print("eixts")
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 1


