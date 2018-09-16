# But, to lock the door he needs a key that is an anagram of a palindrome. He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome.
#
# For example, given the string , one way it can be arranged into a palindrome is .
#
# Function Description
#
# Complete the gameOfThrones function below to determine whether a given string can be rearranged into a palindrome. If it is possible, return YES, otherwise return NO.
#
# gameOfThrones has the following parameter(s):
#
# s: a string to analyze
# Input Format
#
# A single line which contains , the input string.
#


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    charMap = dict()
    for item in s:
        if item in charMap:
            charMap[item] += 1
        else:
            charMap[item] = 1

    oddCounter = 0
    keys = charMap.keys()

    for key in keys:
        if oddCounter > 1:
            return "NO"
        if charMap[key] % 2 != 0:
            oddCounter += 1
    return "YES"

if __name__ == '__main__':
    s: str = "cdcdcdcdeeeef"
    print(gameOfThrones(s))
