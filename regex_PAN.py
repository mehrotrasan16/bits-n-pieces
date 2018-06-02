##https://www.hackerrank.com/challenges/valid-pan-format/problem
import re

nlines = int(raw_input())
ids = []
for line in range(nlines):
    ids.append(raw_input())

rex = r'^([A-Z]{5})([0-9]{4})([A-Z])$'

#print(str(bool(re.search(Regex_Pattern, input()))).lower())
ret_val = []
for i in ids:
    if bool(re.search(rex, i)) == True:
        ret_val.append("YES")
    else:
        ret_val.append("NO")

for i in ret_val:
    print(i.upper())
