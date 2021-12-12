#!/bin/python3

import math
import os
import random
import re
import sys

def arrayManipulation(n, q):
    arr = [0] * (n + 2)
    for a, b, k in q:
        arr[a] += k
        arr[b + 1] -= k
    val_m = 0
    temp = 0
    for i in arr:
        temp += i
        val_m = max(val_m, temp)
    return val_m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
