# 주유소
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))

result = dist[0] * cost[0]

minn = min(cost[:-1])
summ = sum(dist) - dist[0]

for i in range(1, len(cost)-1):
    if cost[i] == minn:
        result += cost[i] * summ
        break
    else:
        result += dist[i] * cost[i]
        summ -= dist[i]

print(result)
