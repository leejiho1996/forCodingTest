# 색종이 올려 놓기
import sys
input = sys.stdin.readline

N = int(input())
papers = []
dp = [0] * N
visited = [0]*(N)

for i in range(N):
    a, b = map(int,input().split())

    if b > a:
        a, b = b, a
        
    papers.append((a,b))

papers.sort()

for i in range(N):
    cur = papers[i][1]
    for j in range(i, -1, -1):
        if cur >= papers[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
    
print(max(dp))