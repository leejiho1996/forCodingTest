# 버스 노선 개편하기
import sys
input = sys.stdin.readline

N = int(input())
routes = []
result = []

for i in range(N):
    S, E, C = map(int,input().split())
    routes.append((S, E, C))

routes.sort()

head, tail, cost = routes[0]

for i in range(1, N):
    s, e, c = routes[i]
    
    if s <= tail:
        tail = max(tail, e)
        cost = min(cost, c)
    else:
        result.append([head, tail, cost])
        head, tail, cost = s, e, c

result.append((head, tail, cost))

print(len(result))

for i in result:
    print(*i)
