# static long power(int x, int n) {
# 	if (n == 0) { return 1; }
# 	if (n % 2 == 0) {
# 		long ans = power(x, n/2);
# 		return ans * ans;
# 	}
# 	else {
# 		return x * power(x, n - 1);
# 	}
# }

def power(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        ans = power(x, n/2)
        return ans * ans

    else:
        return x * power(x, n-1)


if __name__ == '__main__':

    print(power(2, 3))
