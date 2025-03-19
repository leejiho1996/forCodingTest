MOD = 10**9 + 7
def solve(a, b, n):
    if n == 1:
        return 1
    else:
        return pow(2, 31 * (n - 1), MOD)

a, b, n = map(int, input().split())
print(solve(a, b, n))
