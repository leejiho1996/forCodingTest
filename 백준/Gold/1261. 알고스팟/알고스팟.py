# 알고스팟
import sys
input = sys.stdin.readline
import heapq as hq

N, M = map(int,input().split())
graph = []
visited = [[10001] * N for _ in range(M)]
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 4방향

for i in range(M):
    graph.append(input().rstrip())

que = []
# 시작지역인 (0, 0) 부터 탐색
hq.heappush(que, (0, 0, 0))

while que:
    cost, r, c = hq.heappop(que)

    # 목적지에 도착했다면 cost 출력하고 break
    if r == M-1 and c == N-1:
        print(cost)
        break

    for dx, dy in direc:
        nr, nc = r + dx, c + dy

        # 범위를 벗어나거나 이미 최소비용으로 갱신하지 못하는 지역은 방문 x
        if nr < 0 or nr >= M or nc < 0 or nc >= N:
            continue
        elif visited[nr][nc] <= cost + int(graph[nr][nc]):
            continue

        # 해당 지역의 비용을 갱신하고 힙큐에 넣는다
        visited[nr][nc] = cost + int(graph[nr][nc])
        hq.heappush(que, (cost+int(graph[nr][nc]), nr, nc))
    

