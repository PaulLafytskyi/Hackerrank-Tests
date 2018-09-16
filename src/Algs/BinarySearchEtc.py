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
