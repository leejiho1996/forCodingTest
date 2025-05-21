# NxM 보드 완주하기
import sys
input = sys.stdin.readline

def backtrack(r, c, cnt, move):
    global result

    if cnt == possible:
        result = min(result, move)
        return

    for dx, dy in direc:
        
        nr, nc = r, c
        stack = []
        
        while True:   
            nr += dx
            nc += dy

            # 주어진 범위를 넘어가거나 방문할 수 없는 경우 break
            if (nr < 0 or nc < 0 or nr >= N or nc >= M):
                break
            elif visited[nr][nc] != 0:
                break

            # 구슬이 이동한 경로를 스택에 다 담아준다
            stack.append((nr, nc))
            visited[nr][nc] = 1

        # 스택에 이동 경로가 있다면 백트래킹 수행하고 visited 다시 0으로 변
        if stack:
            backtrack(nr-dx, nc-dy, cnt+len(stack), move+1)

            while stack:
                rr, rc = stack.pop()
                visited[rr][rc] = 0

Case = 1
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

try :
    while True:
        N, M = map(int,input().split())
        graph = []
        visited = [[0] * M for _ in range(N)]
        result = 1000001
        possible = -1
        
        for i in range(N):
            row = list(input().rstrip())
            graph.append(row)
            for j in range(M):
                if row[j] == "*":
                    visited[i][j] = 3
                else:
                    possible += 1

        for i in range(N):
            for j in range(M):
                if visited[i][j] == 3:
                    continue
                else:
                    visited[i][j] = 1
                    backtrack(i, j, 0, 0)
                    visited[i][j] = 0

        if result == 1000001:
            print(f'Case {Case}: -1')
        else:
            print(f'Case {Case}: {result}')

        Case += 1
except:
    pass
