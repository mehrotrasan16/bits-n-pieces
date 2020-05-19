#Problem Statement: Calculate the weighted standard deviation and variance for a given array of integers
#Modification of https://www.hackerrank.com/challenges/s10-standard-deviation/problem

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
weights = [int(i) for i in input().split()]

product = [i*j for i,j in zip(array,weights)]
weighted_mean = round(sum(product)/sum(weights),1)

half_num_term = [(x-weighted_mean)**2 for x in array]
num_term = [i*j for i,j in zip(weights,half_num_term)]


nprime = len([i for i in weights if i != 0])
den_term = ((nprime - 1)*sum(weights))/nprime

sum_num = sum(num_term)
wtd_std_nist = round(((sum_num)/den_term)**0.5,1)
wtd_std = round((sum_num/n)**0.5,1)
print(weighted_mean)
print(wtd_std_nist)
print(wtd_std)


##Evaluation
#Compare to numpys implementation
##ans found on stack overflow.
#Eric O Lebigot: How about the following short "manual calculation"?

def weighted_avg_and_std(values, weights):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    """
    average = numpy.average(values, weights=weights)
    # Fast and numerically precise:
    variance = numpy.average((values-average)**2, weights=weights)
    return (average, math.sqrt(variance))
