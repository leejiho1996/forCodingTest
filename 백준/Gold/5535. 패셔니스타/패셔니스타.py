# 패셔니스타
import sys
input = sys.stdin.readline

D, N = map(int,input().split())

temp = []
minn = [101] * 101
maxx = [0] * 101

dp = [[0] * 2 for _ in range(D)]

for i in range(D):
    temp.append(int(input()))

for i in range(N):
    l, h, v = map(int,input().split())

    for j in range(l , h+1):
        minn[j] = min(minn[j], v)
        maxx[j] = max(maxx[j], v)

min_total = 0
max_total = 0

for i in range(1, D):
    cur_maxx = maxx[temp[i]]
    cur_minn = minn[temp[i]]
    prev_maxx = maxx[temp[i-1]]
    prev_minn = minn[temp[i-1]]
    
    dp[i][0] = max(dp[i-1][0] + abs(cur_minn-prev_minn), dp[i-1][1] + abs(cur_minn - prev_maxx))
    dp[i][1] = max(dp[i-1][0] + abs(cur_maxx - prev_minn), dp[i-1][1] + abs(cur_maxx - prev_maxx))
    
    
print(max(dp[D-1][0], dp[D-1][1]))
