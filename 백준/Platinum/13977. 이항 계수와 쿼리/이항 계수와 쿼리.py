# 이항 계수와 쿼리
import sys
input = sys.stdin.readline

def init():
    for i in range(1, 4_000_001):
        dp[i] = (dp[i-1] * i) % MOD 

def cal(num, power):

    if power == 1:
        return num

    res = cal(num, power//2)

    if power % 2 == 1:
        return res * res * num % MOD
    else:
        return res* res % MOD

dp = [0] * (4_000_001 * 4)
dp[0] = 1
MOD = 1_000_000_007

init()

N = int(input())

for i in range(N):
    A, B = map(int,input().split())
    print(dp[A] * cal(dp[B]*dp[A-B], MOD-2) % MOD)

