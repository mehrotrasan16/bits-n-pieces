#Problem: calculate the weighted mean of an array of integers given their weights.
#https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# Objective
# In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given an array, , of  integers and an array, , representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of  decimal place (i.e.,  format).

# Input Format

# The first line contains an integer, , denoting the number of elements in arrays  and .
# The second line contains  space-separated integers describing the respective elements of array .
# The third line contains  space-separated integers describing the respective elements of array .

# Constraints

# , where  is the  element of array .
# , where  is the  element of array .
# Output Format

# Print the weighted mean on a new line. Your answer should be rounded to a scale of  decimal place (i.e.,  format).

# Sample Input

# 5
# 10 40 30 50 20
# 1 2 3 4 5
# Sample Output

# 32.0


n = int(input())
array = map(int,input().split())
weights = [int(i) for i in input().split()]
product = [i*j for i,j in zip(array,weights)]
weighted_mean = round(sum(product)/sum(weights),1)
print(weighted_mean)
