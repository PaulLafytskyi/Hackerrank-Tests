#!/bin/python3
import sys


def hourglassSum(a):
    maxSum = -sys.maxsize - 1
    sum = []
    for i in range(4):
        for j in range(4):
            sum = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][
                j + 2]
            if sum > maxSum:
                maxSum = sum
    return maxSum

if __name__ == '__main__':
    a = []
    for arr_i in range(6):
        arr_temp = list(map(int, input().strip().split(' ')))
        a.append(arr_temp)
    print(hourglassSum(a))
