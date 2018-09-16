

def test():
    s1 = list(set("hello"))
    s2 = list(set("world"))
    s1len = len(s1)
    s2len = len(s2)

    for i in range(s1len):
        print(i)
        for b in range(s2len):

            if s1[i] == s2[b]:
                return 'YES'
            if s1[s1len - (i + 1)] == s2[s2len - b + 1]:
                return 'YES'
    return 'NO'


    for item in a:
        for item2 in b:
            if item == item2:
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    print(test())