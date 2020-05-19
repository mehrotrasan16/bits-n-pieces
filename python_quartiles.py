#problem statement: given an array of integers, calculate the first, second and third quartiles of the array
#URL: https://www.hackerrank.com/challenges/s10-quartiles/problem

# Objective
# In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.

# Input Format

# The first line contains an integer, , denoting the number of elements in the array.
# The second line contains  space-separated integers describing the array's elements.

# Constraints

# , where  is the  element of the array.
# Output Format

# Print  lines of output in the following order:

# The first line should be the value of .
# The second line should be the value of .
# The third line should be the value of .
# Sample Input

# 9
# 3 7 8 5 12 14 21 13 18
# Sample Output

# 6
# 12
# 16

 # Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
array = sorted([int(i)for i in input().split()])

medianarr = (array[n // 2] + array[-(n//2 + 1)]) / 2

mid = 0


if(n%2 != 0):
   mid = round(n/2)+1
else:
    mid = round(n/2)

if(n%2 == 0):
    upper_half = array[:mid]
else:
    upper_half = array[:mid-1]
#print(upper_half)
medh = (upper_half[len(upper_half) // 2] + upper_half[-(len(upper_half)//2 + 1)]) / 2

lower_half = array[mid:]
#print(lower_half)
medl = (lower_half[len(lower_half)// 2] + lower_half[-(len(lower_half)//2 + 1)]) / 2

print(round(medh))
print(round(medianarr))
print(round(medl))


