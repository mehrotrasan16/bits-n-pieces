#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = 1
    j = 0
    while(i <= n):
        j = n-i
        print "".join([j*" ",i*"#"])
        i += 1
        
if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
