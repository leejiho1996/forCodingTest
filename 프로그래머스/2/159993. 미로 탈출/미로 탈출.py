from collections import deque

def bfs(que, destination, visited, maps, row, col):
    direc = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while que:
        x, y, cnt = que.popleft()
        
        for r, c in direc:
            nx = x + r
            ny = y + c
            
            if not (0 <= nx < row) or not (0 <= ny < col) :
                continue
            
            if visited[nx][ny] or maps[nx][ny] == "X":
                continue
            
            if maps[nx][ny] == destination:
                return cnt + 1
                
            visited[nx][ny] = 1
            que.append((nx, ny, cnt+1))
            
    return -1

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] == "S":
                s = (i, j)
            if maps[i][j] == "L":
                l = (i, j)
            if maps[i][j] == "E":
                e = (i, j)
    
    eque = deque() # E를 찾을 큐
    lque = deque() # L을 찾을 큐
    lque.append((s[0], s[1], 0))
    visited = [[0] * col for _ in range(row)]
    
    Lcount = bfs(lque, "L", visited, maps, row, col)
    if Lcount == -1:
        return -1
    
    eque.append((l[0], l[1], Lcount))
    visited = [[0] * col for _ in range(row)]
    Ecount = bfs(eque, "E", visited, maps, row, col)

    return Ecount