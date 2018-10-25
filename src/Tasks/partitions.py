def partition(n, d, depth=0):
    if d == depth:
        return [[]]
    return [
        item + [i]
        for i in range(n+1)
        for item in partition(n-i, d, depth=depth+1)
        ]


# extend with n-sum(entries)
if __name__ == '__main__':
    n = 5
    d = 3
    lst = [[n - sum(p)] + p for p in partition(n, d - 1)]
    print(lst)


