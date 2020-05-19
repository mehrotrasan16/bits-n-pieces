# #Problem Statement: https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# Objective
# In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given an array, , of  integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

# Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of  decimal place (i.e., ,  format).

# Input Format

# The first line contains an integer, , denoting the number of elements in the array.
# The second line contains  space-separated integers describing the array's elements.

# Constraints

# , where  is the  element of the array.
# Output Format

# Print  lines of output in the following order:

# Print the mean on a new line, to a scale of  decimal place (i.e., , ).
# Print the median on a new line, to a scale of  decimal place (i.e., , ).
# Print the mode on a new line; if more than one such value exists, print the numerically smallest one.
# Sample Input

# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
# Sample Output

# 43900.6
# 44627.5
# 4978

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
l = []
l += [int(i) for i in input().split()]
sortl =  sorted(l)

#print(n, l, sum(l))
sums = sum(l)
mean = sums/n
median = (sortl[n // 2] + sortl[-(n//2 + 1)]) / 2
mode = sorted(sorted(Counter(l).items()), key = lambda x: x[1], reverse = True)[0][0]

print(mean)
print(median)
print(mode)
