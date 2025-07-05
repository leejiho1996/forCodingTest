# 울타리
import sys
input = sys.stdin.readline
import time

N = int(input())
fences = list(map(int,input().split()))
fences.sort()

triangles = []
dp = [-1] * (1 << (N+1))

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if fences[k] >= fences[i] + fences[j]:
                continue
            A = fences[k]; B = fences[i]; C = fences[j];
            
            p = (A + B + C) / 2
            area = (p * (p-A) * (p - B) * (p - C))**0.5
            bit = 0
            bit |= (1 << i | 1 << j | 1 << k)
            triangles.append((bit, area))

def dfs(cur):

    if dp[cur] != -1:
        return dp[cur]
    else:
        dp[cur] = 0

    for bit, area in triangles:
        nextt = cur | bit

        if nextt.bit_count() - cur.bit_count() != 3:
            continue

        dp[cur] = max(dp[cur], dfs(nextt) + area)

    return dp[cur]

print(dfs(0))
