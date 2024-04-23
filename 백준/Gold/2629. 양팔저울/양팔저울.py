# 양팔저울
import sys
input = sys.stdin.readline

w = int(input())
weight = list(map(int,input().split()))

b = int(input())
beed = list(map(int,input().split()))

dp = [[0 for _ in range(i * 500 + 1)] for i in range(w+1)]

def scale(n, summ):
    
    if dp[n][summ]:
        return
    
    dp[n][summ] = 1

    if n == w:
        return
    
    scale(n+1, summ+weight[n])
    scale(n+1, summ)
    scale(n+1, abs(summ-weight[n]))

scale(0, 0)
            
for i in beed:
    if i > 15000:
        print("N", end = ' ')
        continue
    
    if dp[w][i]:
        print("Y", end = ' ')
    else:
        print("N", end = ' ')