
def calculate(array, sortedArray):
    hashTable = {}
    for i in range(len(array)):
        hashTable[array[i]] = i
    counter = 0

    for j in range(len(array)):
        if array[j] != sortedArray[j]:
            counter += 1
            index = hashTable[sortedArray[j]]
            hashTable[array[j]] = hashTable[sortedArray[j]]
            array[j], array[index] = sortedArray[j], array[j]
    return counter

if __name__ == '__main__':
    N = int(input())
    array = [int(i) for i in input().split(" ")]
    sortedArray = sorted(array)
    normal = calculate(array[::], sortedArray)
    revers = calculate(array[::-1], list(sortedArray))
    print(min(normal, revers))