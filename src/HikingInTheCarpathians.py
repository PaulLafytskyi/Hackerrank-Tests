import sys
def solve(way):
    lastStop = way[-1]
    results = sys.maxsize
    indexToRemove = 0

    for i in range(0, len(way)):
        t = max(way[0] + way[i], lastStop - way[i])
        if t > 0 and t <= results:
            results = t
            indexToRemove = i
    return results, indexToRemove

if __name__ == '__main__':
    way = [0, 4, 5, 11, 12]
    stops = 2
    finalResult = 0
    itr = -1
    for i in range(stops):
        r, itr = solve(way)
        if r != sys.maxsize and itr != 0:
            finalResult = r
            way = way[:itr+]
    print(finalResult)