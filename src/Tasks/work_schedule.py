#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:17:22 2018

@author: owen
"""

import datetime
# Visa OA

def findSchedules(workHours, dayHours, pattern):


    def dfs(target, day_limit, partial_sum, start, remain, curr, res):
        print(partial_sum, start,remain,curr,res)
        if remain == 0:  # no ? remains
            if sum(curr) == target:
                res.append("".join(map(str, curr)))
            return

        if partial_sum > target:  # pruning
            return
        for day in range(start, 7):
            if curr[day] == '?':
                for hour in range(day_limit + 1):  # traverse all possible day work hour from 0
                    curr[day] = hour
                    dfs(target, day_limit, partial_sum + hour, day + 1, remain - 1, curr, res)
                curr[day] = '?'





    if workHours > 56 or dayHours > 8 or len(pattern) != 7:
        return 0

    curr = []  # convert to integers + '?', then directly calculate sum, and convert to string for final result
    length = 7  # how many ? need to replace
    partial_sum = 0
    for c in pattern:
        if c != '?':
            length -= 1
            curr.append(int(c))
            partial_sum += int(c)
        else:
            curr.append(c)

    res = []
    dfs(workHours, dayHours, partial_sum, 0, length, curr, res)
    return res


# def findSchedules(workHours, dayHours, pattern):
#    # Write your code here
#    # Permutation, time O(dayHours^7), slower
#    def dfs(target, day_limit, start, remain, curr, res):
#        if remain == 0: # no ? remains
#            if sum(map(int, curr)) == target:
#                res.append("".join(curr))
#            return
#
#        for day in range(start, 7):
#            if curr[day] == '?':
#                for hour in range(day_limit + 1): # traverse all possible day work hour from 0
#                    curr[day] = str(hour)
#                    dfs(target, day_limit, day + 1, remain - 1, curr, res)
#                curr[day] = '?'
#
#
#    if workHours > 56 or dayHours > 8 or len(pattern) != 7:
#        return 0
#
#    curr = list(pattern) # convert to string, then convert it to integers when comparing with target
#    length = 7 # how many ? need to replace
#    for c in pattern:
#        if c != '?':
#            length -= 1
#
#    res = []
#    dfs(workHours, dayHours, 0, length, curr, res)
#    return res


def partitions(n):
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n - 1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]


if __name__ == "__main__":
    a = partitions(5)
    for i in a:
        print(i)




# print(datetime.datetime.now())
# # print(findSchedules(56, 8, "???8???"))
# print(findSchedules(24, 4, "08??840"))
# print(datetime.datetime.now())
