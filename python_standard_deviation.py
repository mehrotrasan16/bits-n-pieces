#Problem Statement: Calculate the standard deviation and variance for a given array of integers
#https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# Objective
# In this challenge, we practice calculating standard deviation. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given an array, , of  integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of  decimal place (i.e.,  format). An error margin of  will be tolerated for the standard deviation.

# Input Format

# The first line contains an integer, , denoting the number of elements in the array.
# The second line contains  space-separated integers describing the respective elements of the array.

# Constraints

# , where  is the  element of array .
# Output Format

# Print the standard deviation on a new line, rounded to a scale of  decimal place (i.e.,  format).

# Sample Input

# 5
# 10 40 30 50 20
# Sample Output

# 14.1

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
array = [int(i) for i in input().split()]
mean = sum(array)/n
num_term = [(x-mean)**2 for x in array]
sum_num = sum(num_term)
variance = round(((sum_num)/n),1)
std = round(((sum_num)/n)**0.5,1)
print(std)