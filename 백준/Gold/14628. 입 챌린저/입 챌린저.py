# 입 챌린저
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())

use_skill = [[0] * (N+1) for _ in range(M+1)]
dp = [float('inf')] * (M+1) # dp[i] -> 체력을 i로 만들기 위한 최소 마나 포인트
dp[M] = 0

skills = []

for i in range(N):
    x, y = map(int,input().split())
    skills.append((x, y))

for i in range(M, -1, -1):
    
    for j in range(N):
        x, y = skills[j]

        if i + y > M:
            continue

        mana_point = x + use_skill[i+y][j] * K
       
        if dp[i] > dp[i+y] + mana_point:
            dp[i] = dp[i+y] + mana_point
            use_skill[i] = use_skill[i+y].copy()
            use_skill[i][j] += 1
      
print(dp[0])
