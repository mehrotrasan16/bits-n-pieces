##https://www.hackerrank.com/challenges/saying-hi/problem
import re

nlines = int(raw_input())
ids = []
for line in range(nlines):
    ids.append(raw_input())

rex = r'^[Hh][Ii]\s[^Dd].*$'


#print(str(bool(re.search(Regex_Pattern, input()))).lower())
ret_val = []
for i in ids:
    if bool(re.search(rex, i)) == True :
        ret_val.append(i)

    

for i in ret_val:
    print(i)
