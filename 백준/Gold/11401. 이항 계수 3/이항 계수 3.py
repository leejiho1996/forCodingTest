# 이항계수3
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (n+1)
dp[0] = 1
mod = 1_000_000_007

for i in range(1, n+1):
    dp[i] = dp[i-1] * i % mod

# 페르마의 소정리 -> a**(p-1) = 1 (mod p)

head = dp[n] 
tail = dp[k] * dp[n-k] % mod

def divide(num, cnt, mod):
    if cnt == 1:
        return num % mod

    result = divide(num, cnt//2, mod)

    if cnt % 2 == 0:
        return  result * result % mod
    else:
        return result * result * num % mod

print(head * divide(tail, mod-2, mod) % mod)