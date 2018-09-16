import sys

if __name__ == '__main__':
    N = int(input())
    array = [int(i) for i in input().split(" ")]
    array.sort()

    min = sys.maxsize
    result = []

    for i in range(len(array)):
        current = array[i]
        prev = array[i-1]
        diff = abs(current - prev)
        if diff < min:
            min = diff
            result = [str(prev), str(current)]
        elif diff == min:
            result.append(str(prev))
            result.append(str(current))


    print(' '.join(result))