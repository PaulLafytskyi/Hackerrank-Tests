
#!/bin/python3

import math
import os
import random
import re
import sys

def helper(nums, start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    if nums[mid] > nums[mid + 1]:
        return helper(nums, start, mid)

    return helper(nums, mid + 1, end)

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(helper(nums, 0, len(nums) - 1))