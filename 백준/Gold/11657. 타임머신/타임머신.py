# 타임 머신
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

route = []

for i in range(m):
    a, b, c = map(int,input().split())
    route.append((a-1, b-1, c))


def bell():
    check = False
    
    visit = [float("inf")] * n
    visit[0] = 0
    
    for i in range(n-1):
        for start, to, cost in route:
            if visit[start] != float('inf') and visit[start] + cost < visit[to]:
                visit[to] = visit[start] + cost

    for start, to, cost in route:
        if visit[start] != float('inf') and visit[start] + cost < visit[to]:
            check = True
            print(-1)
            break

    if not check:
        for i in range(1, n):
            if visit[i] == float('inf'):
                print(-1)
            else:
                print(visit[i])
bell()
