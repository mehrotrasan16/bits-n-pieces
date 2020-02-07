##Problem: to remove vowels from a string

import re

string_str = "PQRSTAEIOUMNOPaedfioghu"
str1ing_str = string_str

x = re.match("[A]",string_str)

while(x is not None):
    print("Match found, vowel removal procedure")
    str1ing_str = str(string_str[0:x.start()] + string_str[x.end():])
    x = re.match("[AEIOUaeiou]",str1ing_str)
    print(f'{str1ing_str}')

print(f'Result String is {str1ing_str}')

#theoretically works but practically, the string fails to match after the slicing

### code from stack overflow for above procedure using regexes
### source: https://stackoverflow.com/questions/21581824/correct-code-to-remove-the-vowels-from-a-string-in-python
import re

def anti_vowel(s):
    result = re.sub(r'[AEIOU]', '', s, flags=re.IGNORECASE)
    return result

print(anti_vowel(string_str))
########################################################

##Shorter and simpler solution without libraries

string_str = 'PQRSTAEIOUMNOPaedfioghu'

for ch in ['a','e','i','o','u','A','E','I','O','U']:
    print(ch)
    print(string_str.replace(ch,''))
    string_str = string_str.replace(ch,'')

print(string_str)
