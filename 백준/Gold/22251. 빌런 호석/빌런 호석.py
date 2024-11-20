# 빌런 호석
import sys
input = sys.stdin.readline

n, k, p, x = map(int,input().split())
dic = {0:[1,1,1,0,1,1,1],
       1:[0,0,1,0,0,1,0],
       2:[1,0,1,1,1,0,1],
       3:[1,0,1,1,0,1,1],
       4:[0,1,1,1,0,1,0],
       5:[1,1,0,1,0,1,1],
       6:[1,1,0,1,1,1,1],
       7:[1,0,1,0,0,1,0],
       8:[1,1,1,1,1,1,1],
       9:[1,1,1,1,0,1,1]
       }

dp = [[0] * 10 for _ in range(10)] # dp[n][m] = n에서 m까지 가는데 필요한 갯수

change = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(i+1, 10):
        cnt = 0
        for k in range(7):
            if dic[i][k] != dic[j][k]:
                cnt += 1
        dp[i][j] = cnt
        dp[j][i] = cnt

cnt = 0
string_x = (k - len(str(x))) * "0" + str(x)

for i in range(1, n+1):
    zero = k - len(str(i))
    cur = zero*"0" + str(i)
    total = 0

    if cur == string_x:
        continue
    
    for j in range(k):
        total += dp[int(cur[j])][int(string_x[j])]

        if total > p:
            break

    if total <= p:
        cnt += 1

print(cnt)
