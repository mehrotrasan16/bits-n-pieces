#https://www.hackerrank.com/challenges/python-time-delta/problem
#Script to read pairs of date-time in the format 
#Day dd Mon yyyy hh:mm:ss +xxxx 
#from a text file . here +xxxx represents the time zone. and to print the absolute difference (in seconds) between them.

#!/bin/python3
import os
from datetime import datetime as dt


# Complete the time_delta function below.
def time_delta(t1, t2):
    puret1 = dt.strptime(t1,"%a %d %b %Y %H:%M:%S %z")

    puret2 =  dt.strptime(t2,"%a %d %b %Y %H:%M:%S %z")

    return str(abs(int((puret1 - puret2).total_seconds())))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
