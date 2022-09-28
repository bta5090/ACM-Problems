#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    p = 0
    n = 0
    z = 0
    
    total = len(arr)
    
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        elif i == 0:
            z += 1
    
    tp = float(p / total)
    tn = float(n / total)
    tz = float(z / total)
    
    print("%.6f" % tp)
    print("%.6f" % tn) 
    print("%.6f" % tz)         

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
