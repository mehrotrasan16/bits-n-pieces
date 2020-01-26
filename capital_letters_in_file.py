##Problem Statement: WAP to read a file and retrurn the number of capital letters in the file
##
##
import os
os.chdir("D:\\User\\SanketM\\Documents")
f = open("Skills.txt","r+")
f.seek(0)
content = f.read()
import re
for ch in content:
	if(re.match("[A-Z]",ch) is not None):
		count+=1
count = 0
for ch in content:
	if(re.match("[A-Z]",ch) is not None):
		count+=1
print(f'The num of capital letters in the file is : {count}')

###################################################################

#Same thing in 4 lines

 string = ""
 for ch in open("Skills.txt","r+").read():
	if(re.match("[A-Z]",ch) is not None):
		string += ch
 len(string)
