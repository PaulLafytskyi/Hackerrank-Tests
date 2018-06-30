def calculate(array):
    l_counter = 0
    r_counter = len(array) - 1
    left_sum = array[l_counter]
    right_sum = array[r_counter]

    while l_counter != r_counter:
        if left_sum < right_sum:
            l_counter += 1
            left_sum += array[l_counter]
        else:
            r_counter -= 1
            right_sum += array[r_counter]

    return left_sum == right_sum

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if calculate(a):
            print('YES')
        else:
            print('NO')