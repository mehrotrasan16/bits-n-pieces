# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string s1

    # A string consisting of lowercase English letters.

    # Guaranteed constraints:
    # 1 ≤ s1.length < 15.

    # [input] string s2

    # A string consisting of lowercase English letters.

    # Guaranteed constraints:
    # 1 ≤ s2.length < 15.

    # [output] integer

from collections import Counter
def commonCharacterCount(s1, s2):
    uniqs1 = Counter(s1)
    uniqs2 = Counter(s2)
    commoncount = 0
    for index, char in enumerate(uniqs1):
        if(char in uniqs2):
            commoncount += min(uniqs1[char],uniqs2[char])
    
    return commoncount
