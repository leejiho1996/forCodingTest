# 주간 달력
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
plans = [0] * 50002
end = [0] * 50001
result = 0

for i in range(M):
    s, e = map(int,input().split())
    end[e] += 1
    plans[s] += 1
    plans[e+1] -= 1

for i in range(2):
    for j in range(1, 50001):
        plans[j] = plans[j-1] + plans[j]

limit = N * 7 
maxx = 0
maxIdx = 0

for i in range(1, 50001-limit+1):
    if plans[i+limit-1] - plans[i-1] > maxx:
        maxx = plans[i+limit-1] - plans[i-1]
        maxIdx = i

cnt = 0
for i in range(maxIdx, maxIdx+limit):
    cnt += 1

    if cnt % 7 == 0:
        result += (plans[i]-plans[i-1]) - end[i]
    
    result += end[i]

print(result)

