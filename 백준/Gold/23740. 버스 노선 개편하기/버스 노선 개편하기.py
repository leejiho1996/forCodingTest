# 버스 노선 개편하기
import sys
input = sys.stdin.readline

N = int(input())
routes = []
result = []

for i in range(N):
    S, E, C = map(int,input().split())
    routes.append((S, E, C))

routes.sort() # 노선들을 오름차순으로 정렬

head, tail, cost = routes[0]

for i in range(1, N):
    s, e, c = routes[i]
    
    if s <= tail: # 노선이 겹치는 경우
        tail = max(tail, e) # 끝나는 부분이 더 먼 것으로 갱신
        cost = min(cost, c) # 비용은 최소로 갱신
    else:
        result.append((head, tail, cost))
        head, tail, cost = s, e, c

# 마지막 노선도 넣어줘야한다.
result.append((head, tail, cost))

print(len(result))

for i in result:
    print(*i)
