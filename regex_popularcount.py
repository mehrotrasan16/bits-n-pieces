##https://www.hackerrank.com/challenges/find-hackerrank/problem
import re

nlines = int(raw_input())
ids = []
for line in range(nlines):
    ids.append(raw_input())

rexbeg = r'^hackerrank.*$'
rexend = r'^.*hackerrank$'


#print(str(bool(re.search(Regex_Pattern, input()))).lower())
ret_val = []
for i in ids:
    if bool(re.search(rexbeg, i)) == True and bool(re.search(rexend, i)) == True:
        ret_val.append(0)
        continue
    elif bool(re.search(rexend, i)) == True:
        ret_val.append(2)
        continue
    elif bool(re.search(rexbeg, i)) == True:
        ret_val.append(1)
        continue
    else:
        ret_val.append(-1)
        continue

    

for i in ret_val:
    print(i)
