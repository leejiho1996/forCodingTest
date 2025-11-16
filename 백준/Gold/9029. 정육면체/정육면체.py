# 정육면체
import sys
input = sys.stdin.readline

def solve(w, h, l):
    
    if dp[w][h][l] != -1:
        return dp[w][h][l]

    if w == h == l:
        dp[w][h][l] = 1
        return 1

    if w == 1 or h == 1 or l == 1:
        dp[w][h][l] = w * h * l
        return w * h * l
    
    ret = float('inf')
        
    for i in range(1, w//2+1):
        ret = min(ret, solve(w-i, h, l) + solve(i, h, l))

    for i in range(1, h//2+1):
        ret = min(ret, solve(w, h-i, l) + solve(w, i, l))

    for i in range(1, l//2+1):
        ret = min(ret, solve(w, h, l-i) + solve(w, h, i))

    dp[w][h][l] = ret
    dp[h][w][l] = ret
    dp[w][l][h] = ret
    dp[h][l][w] = ret
    dp[l][h][w] = ret
    dp[l][w][h] = ret

    return ret

dp = [[[-1] * 201 for _ in range(201)] for _ in range(201)]

N = int(input())

for i in range(N):
    W, L, H = map(int,input().split())
    print(solve(W, H, L))
