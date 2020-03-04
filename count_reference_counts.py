## Problem Statement: WAP that counts the number of references present
## in the given text of a paper and plots it
## to infer what paper might be construed as the most important
## or most referred paper in the given paper.

import os

os.chdir("D:\\User\\tmp\\")         ## directory with the text of the paper
f = open("Paper Test 2", mode='r+', encoding="utf8")  ## I just copied and pasted the text from a pdf into a text file
f.seek(0)   ##reset file ptr location

#init d
d = {}

#d[0] = "Test Ref" 


for num in range(1,50):     ## number of references in the paper
    print(num)
    f.seek(0)       
    for line in f:          ## read the file line by line
	#print(line)
	#print("["+str(num)+"]")
	#print(line.find("["+str(num)+"]"))
        if line.find("["+str(num)+"]") > 0 :
            print("exists")
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 1

print(d)

import matplotlib.pyplot as plt

#plt.plot(list(d.keys()),list(d.values())) ## plot the reference and its counts
## todo: try a historgram
plt.stem(list(d.keys()),list(d.values())) ## plot a stem plot of the reference and its counts
plt.xticks(list(d.keys()))
plt.show()
