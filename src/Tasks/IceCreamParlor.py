# Ice Cream Parlor Hackerrank
# Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool together m dollars
# for ice cream. On any given day, the parlor offers a line of n flavors. Each flavor, i,
# is numbered sequentially with a unique ID number from 1 to n and has a cost, ci, associated with it.
#
# Given the value of m and the cost of each flavor for t trips to the Ice Cream Parlor,
# help Sunny and Johnny choose two flavors such that they spend their entire pool of money (m) during each visit.
# For each trip to the parlor, print the ID numbers for the two types of ice cream that
# Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.
#
# Note: Two ice creams having unique IDs i and j may have the same cost (i.e., ci = cj).
#
#

def binary_search(a, x):
    l = -1
    r = len(a)
    while (r - l) > 1:
        m = (l + r) // 2
        if a[m] > x:
            r = m
        else:
            l = m
    if l >= 0 and a[l] == x:
        return l
    return -1

def quickSort(array):
    qsortHelper(array, 0, len(array) - 1)

def qsortHelper(array, lo, hi):
    if (hi <= lo):
        return
    splitPoint = partition(array, lo, hi)
    qsortHelper(array, lo, splitPoint - 1)
    qsortHelper(array, splitPoint + 1, hi)


def partition(alist, first, last):
    pivot = alist[first]
    leftMark = first + 1
    rightMark = last

    done = False

    while not done:
        while leftMark <= rightMark and alist[leftMark] <= pivot:
            leftMark += 1
        while alist[rightMark] >= pivot and rightMark >= leftMark:
            rightMark -= 1
        if rightMark < leftMark:
            done = True
        else:
            temp = alist[leftMark]
            alist[leftMark] = alist[rightMark]
            alist[rightMark] = temp

    temp = alist[first]
    alist[first] = alist[rightMark]
    alist[rightMark] = temp

    return rightMark


def solve():
    m = int(input())
    n = int(input())
    a = [int(i) for i in input().split(" ")]

    sortedCosts = a.copy()
    quickSort(sortedCosts)
    for i in range(n):
        sumLeft = m - a[i]
        if sumLeft > 0:
            bindex = binary_search(sortedCosts, sumLeft)
            if bindex > 1:
                index = a.index(sumLeft)
                print(i + 1, index + 1)
                break

if __name__ == '__main__':
    tripsNumber = int(input())
    for t in range(tripsNumber):
        solve()


