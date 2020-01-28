##Problem: to remove vowels from a string

import re

string_str = "PQRSTAEIOUMNOPaedfioghu"
str1ing_str = string_str

x = re.match("[A]",string_str)
print(x)

while(x is not None):
    print("Match found, vowel removal procedure")
    str1ing_str = str(string_str[0:x.start()] + string_str[x.end():])
    x = re.match("[AEIOUaeiou]",str1ing_str)
    print(f'{str1ing_str}')

print(f'Result String is {str1ing_str}')

#theoretically works but practically, the string fails to match after the slicing
########################################################

##Shorter and simpler solution without libraries

string_str = 'PQRSTAEIOUMNOPaedfioghu'

for ch in ['a','e','i','o','u','A','E','I','O','U']:
    print(ch)
    print(string_str.replace(ch,''))
    string_str = string_str.replace(ch,'')

print(string_str)
