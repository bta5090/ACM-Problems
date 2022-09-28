#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    large = -10000000000
    small = 100000000000
    size = len(arr)
    s = 0
    
    for i in range(0, size):
        
        if i == 0:
            s = sum(arr[1:size])
        elif i == size - 1:
            s = sum(arr[:i])
        else:
            s = sum(arr[:i]) + sum(arr[i+1:])
        
        if s > large:
            large = s
        
        if s < small:
            small = s
    
    
    print(small, large)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
