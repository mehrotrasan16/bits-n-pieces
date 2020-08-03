# 20. Valid Parentheses
# Easy

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')':'(', '}':'{',']':'['}
        stack = []
        
        for i in s:
            
            #if i is a opening bracket, append it
            if i in d.values():
                stack.append(i)
            
            #if i is a closing bracket, pop the stack, if its the same type then okay else False. 
            # also if the stack is empty and the first character is a close then False
            elif not stack or stack.pop() != d[i]:
                return False
            
        return not stack