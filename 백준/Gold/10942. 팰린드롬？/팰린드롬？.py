import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n-i):
        start = j
        end = j + i
        if start == end:
            dp[start][end] = 1
            continue

        if num[start] == num[end]: 
            if end - start == 1 or dp[start+1][end-1]:
                dp[start][end] = 1

m = int(input())
for i in range(m):
    start, end = map(int,input().split())
    start -= 1
    end -= 1
    
    print(dp[start][end])