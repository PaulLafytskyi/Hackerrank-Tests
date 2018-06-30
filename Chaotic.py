def read_strings():
    return input().strip().split(' ')

def read_ints():
    return [int(x) for x in read_strings()]

def minimumBribes(q):
    count = 0
    for i in range(len(q)):
        dif = i + 1 - q[i]
        if (dif < -2):
            print("Too chaotic")
            return
        else:
            if dif > 0:
                count += 1
    print(count)


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t = int(input())
        if(t == 0):
            print(0)
        else:
            minimumBribes(read_ints())