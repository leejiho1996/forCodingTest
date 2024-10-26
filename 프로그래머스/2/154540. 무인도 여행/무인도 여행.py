import sys
sys.setrecursionlimit(100000)

def dfs(maps, visited, i, j, row, col):
    total = int(maps[i][j])
    direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for x, y in direc:
        nx = i + x
        ny = j + y

        if not (0 <= nx < row) or not (0 <= ny < col) :
            continue
        
        if maps[nx][ny] == "X" or visited[nx][ny]:
            continue
            
        visited[nx][ny] = 1
        total += dfs(maps, visited, nx, ny, row, col)
        
    return total

def solution(maps):
    answer = []
    row = len(maps)
    col = len(maps[0])
    visited = [[0] * col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] != "X" and visited[i][j] == 0:
                visited[i][j] = 1
                answer.append(dfs(maps, visited, i, j, row, col))
    
    if len(answer) == 0:
        answer.append(-1)
        
    answer.sort()
    return answer