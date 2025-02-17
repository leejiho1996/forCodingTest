# 2048 easy
import sys
input = sys.stdin.readline

def isOut(r, c):
    if r < 0 or c < 0 or r >= n or c >= n:
        return True
    else:
        return False
    
def move(call, dx, dy, rs, re, cs, ce, graph):
    if rs > re:
        rSep = -1
    else:
        rSep = 1

    if cs > ce:
        cSep = -1
    else:
        cSep = 1
        
    for i in range(rs, re, rSep):
        for j in range(cs, ce, cSep):
            if graph[i][j] == 0:
                continue

            cur = graph[i][j]
            r = i
            c = j
            while True:
                if isOut(r+dx, c+dy):
                    break
                elif graph[r+dx][c+dy] == 0:
                    graph[r+dx][c+dy] = cur
                    graph[r][c] = 0
                elif graph[r+dx][c+dy] == cur and visited[r+dx][c+dy] != call:
                    visited[r+dx][c+dy] = call
                    graph[r+dx][c+dy] = cur*2
                    graph[r][c] = 0
                else:
                    break

                r += dx
                c += dy

def backtrack(cnt, graph):
    global result
    global callCount

    callCount += 1
    
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                result = max(result, graph[i][j])

        return
        
    for i in range(4):
        nGraph = []
        for j in range(n):
            nGraph.append(graph[j].copy())

        dx, dy = direc[i]
        rs, re, cs, ce = forElement[i]
        move(callCount, dx, dy, rs, re, cs, ce, nGraph)
        backtrack(cnt+1, nGraph)
        
n = int(input())
graph = []
visited = [[0] * n for _ in range(n)]
result = 0
callCount = 0

# 아래, 위, 오른쪽, 왼쪽으로 이동
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
forElement = [(n-1, -1, 0, n), (0, n, 0, n), (0, n, n-1, -1), (0, n, 0, n)]

for i in range(n):
    graph.append(list(map(int,input().split())))

backtrack(0, graph)

print(result)

