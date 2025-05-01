# 도미노 찾기
import sys
input = sys.stdin.readline

graph = [list(map(int, list(input().rstrip()))) for _ in range(8)]
dominos = [[0] * 7 for _ in range(7)]
visited = [[0] * 7 for _ in range(8)]
result = 0

def backtrack(cnt, total):
    global result

    if total == 56:
        result += 1
        return

    r = cnt // 7
    c = cnt % 7

    if visited[r][c]:
        backtrack(cnt+1, total)
        return

    for dx, dy in [(0, 1), (1, 0)]:
        nr, nc = r+dx, c+dy

        if nr >= 8 or nc >= 7:
            continue

        if visited[nr][nc]:
            continue
        
        n1 = graph[r][c]
        n2 = graph[nr][nc]

        if dominos[n1][n2] == 0 or dominos[n2][n1] == 0:
            dominos[n1][n2] = 1
            dominos[n2][n1] = 1
            visited[r][c] = 1
            visited[nr][nc] = 1

            backtrack(cnt+1, total+2)

            dominos[n1][n2] = 0
            dominos[n2][n1] = 0
            visited[r][c] = 0
            visited[nr][nc] = 0

backtrack(0, 0)
print(result)
        
