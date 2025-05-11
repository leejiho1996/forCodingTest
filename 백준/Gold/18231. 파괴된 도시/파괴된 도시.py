# 파괴된 도시
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = []

for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

K = int(input())
broken = list(map(int,input().split()))
broken.sort()

# 파괴된 도시를 따로 체크
for i in broken:
    visited[i] = 1

# 폭탄 맞은 도시를 저장
possible = set()

for i in broken:
    check = False
    
    for j in graph[i]:
        # 주변도시가 파괴되지 않앗다면 폭탄 맞은 도시가 아니다
        if visited[j] == 0:
            check = True
            break

    if not check:
        # 폭탄 맞은 도시일 경우 주변 도시도 파괴되니 저장
        possible.add(i)
        result.append(i)
        for j in graph[i]:
            possible.add(j)

# 주어진 정보와 계산한 정보가 다르면 -1
if len(possible) != K:
    print(-1)
else:
    print(len(result))
    print(*result)
