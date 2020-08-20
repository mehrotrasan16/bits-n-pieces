# ~ Power of Four
# ~ Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# ~ Example 1:

# ~ Input: 16
# ~ Output: true
# ~ Example 2:

# ~ Input: 5
# ~ Output: false
# ~ Follow up: Could you solve it without loops/recursion?

#import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        #works for positive numbers only
        # log = math.log(num,4)
        # if math.ceil(log) == math.floor(log):
        #     return True
        # else:
        #     return False
        
        #way to convert number to binary without the 0b\0x in the beg
        # works with o - octal, x - hex, and d - dec
        
        # bin = "{0:b}".format(num)
        
        if(bin(num)[0] == "-"):
            return False
        if(bin(num)[2:].count('1') == 1 and (bin(num)[2:].count('0'))%2 == 0):
            return True
        else:
            return False
