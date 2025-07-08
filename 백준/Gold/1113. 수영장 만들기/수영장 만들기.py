import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c, height):

    visited[r][c] = 1
    que = deque([(r, c)])
    check = True
    ret = 0
    
    while que:
        r, c = que.popleft()
        # 물을 채울 수 있는 만큼 ret에 더해주고 현재위치의 높이를 바꿔준다  
        ret += 1
        graph[r][c] = height
                
        for dr, dc in direc:
            nr, nc = r + dr, c + dc
            # 주어진 범위를 벗어나면 물이 밖으로 샌다는 의미
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                check = False
                continue

            if visited[nr][nc]:
                continue

            # 물은 낮은 곳으로 흐르므로 현재 위치보다 낮은 경우만 탐색
            if graph[nr][nc] < height:
                que.append((nr, nc))
                visited[nr][nc] = 1
                
    
    if check: # 물이 밖으로 새는 경우가 없다면 계산한 값 리턴
        return ret
    else: # 밖으로 새는 경우가 있다면 0리턴
        return 0

N, M = map(int, input().split())
graph = []
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 4방향 이동
result = 0

for i in range(N):
    row = list(input().rstrip())
    graph.append(list(map(int, row)))
    
for k in range(2, 10): # 2부터 9까지 채운다
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j]: # 이미 체크한 지역은 패스
                continue
            # 현재 지역의 높이가 채우고자 하는 k보다 낮을때만 탐색
            if graph[i][j] < k: 
                result += bfs(i, j, k)

print(result)
