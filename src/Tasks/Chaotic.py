#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    result = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        c = max(0, q[i] - 2)
        for j in range(c, i):
            if q[j] > q[i]:
                result += 1
    print(result)

if __name__ == '__main__':
    minimumBribes([2, 1, 5, 3, 4])
