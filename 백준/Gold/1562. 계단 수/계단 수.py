# 계단수
import sys
input= sys.stdin.readline

def getCount(cnt, last, visit):
    if cnt == n:
        if visit == (1 << 10) - 1:
            dp[cnt][last][visit] = 1
            return 1
        else:
            dp[cnt][last][visit] = 0
            return 0

    if dp[cnt][last][visit] != -1:
        return dp[cnt][last][visit]
    else:
        dp[cnt][last][visit] = 0
        
    if last == 0:
        dp[cnt][last][visit] += getCount(cnt+1, 1, visit | (1 << 1)) % MOD
    elif last < 9:
        dp[cnt][last][visit] += getCount(cnt+1, last-1, visit | (1 << (last-1))) % MOD
        dp[cnt][last][visit] += getCount(cnt+1, last+1, visit | (1 << (last+1))) % MOD
    elif last == 9:
        dp[cnt][last][visit] += getCount(cnt+1, last-1, visit | (1 << (last-1))) % MOD

    return dp[cnt][last][visit] % MOD

n = int(input())
dp = [[[-1] * (1 << 10) for _ in range(10)] for _ in range(n+1)]
total = 0
MOD = 1_000_000_000

for i in range(1, 10):
    total += getCount(1, i, 1 << i)
    total %= MOD
    
print(total)
