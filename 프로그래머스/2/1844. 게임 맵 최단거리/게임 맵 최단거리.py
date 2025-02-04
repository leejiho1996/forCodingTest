from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    direc = [(1,0), (-1,0), (0,1), (0,-1)]
    visited = [[n*m+1] * m for _ in range(n)]
    que = deque([(0, 0, 1)])
    
    while que:
        r, c, cnt = que.popleft()
        
        if r == n-1 and c == m-1:
            return cnt
        
        if cnt >= visited[r][c]:
            continue
        else:
            visited[r][c] = cnt
            
        for x, y in direc:
            nr, nc = r + x, c + y
            
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            elif maps[nr][nc] == 0 or visited[nr][nc] <= cnt + 1:
                continue
            else:
                que.append((nr, nc, cnt+1))
    
    return -1