# 동전 분배
import sys
input = sys.stdin.readline

for i in range(3):
    n = int(input())
    coins = []
    total = 0
    for j in range(n):
        coin, amount = map(int,input().split())
        total += coin * amount
        coins.append((coin, amount))
    
    if total % 2 == 1:
        print(0)
        continue

    half = total // 2
    dp = [0] * (half+1)
    dp[0] = 1

    for i in range(n):
        coin = coins[i][0]
        amount = coins[i][1]
        for j in range(half, coin-1, -1):
            if dp[j-coin]:
                  for k in range(amount):
                    if j + k * coin > half:
                        break
                    dp[j+k*coin] = 1
    
    if dp[half]:
        print(1)
    else:
        print(0)
    
