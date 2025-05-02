# 주간 달력
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
plans = [0] * 50001
end = [0] * 50001
aggSum = [0] * 50001
result = 0

for i in range(M):
    s, e = map(int,input().split())
    end[e] += 1
    
    for j in range(s, e+1):
        plans[j] += 1

for i in range(1, 50001):
    aggSum[i] = aggSum[i-1] + plans[i]

limit = N * 7 
maxx = 0
maxIdx = 0

for i in range(1, 50001-limit+1):
    if aggSum[i+limit-1] - aggSum[i-1] > maxx:
        maxx = aggSum[i+limit-1] - aggSum[i-1]
        maxIdx = i

cnt = 0
for i in range(maxIdx, maxIdx+limit):
    cnt += 1

    if cnt % 7 == 0:
        result += plans[i] - end[i]
    
    result += end[i]

print(result)

