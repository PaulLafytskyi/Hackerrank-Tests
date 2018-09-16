import math

if __name__ == '__main__':
    n = int(input())
    a = ""
    for _ in range(n):
        x = int(input())
        answer = math.sqrt(8*x - 7)
        d = answer % 1 == 0
        if d:
            a += ("1" + " ")
        else:
            a += ("0" + " ")

    print(a)