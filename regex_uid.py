##https://www.hackerrank.com/challenges/utopian-identification-number/problem
import re

nlines = int(raw_input())
ids = []
for line in range(nlines):
    ids.append(raw_input())

rex = r'^([a-z]{0,3})([0-9]{2,8})([A-Z]{3,})$'

#print(str(bool(re.search(Regex_Pattern, input()))).lower())
ret_val = []
for i in ids:
    if bool(re.search(rex, i)) == True:
        ret_val.append("Valid")
    else:
        ret_val.append("Invalid")

for i in ret_val:
    print(i.upper())
