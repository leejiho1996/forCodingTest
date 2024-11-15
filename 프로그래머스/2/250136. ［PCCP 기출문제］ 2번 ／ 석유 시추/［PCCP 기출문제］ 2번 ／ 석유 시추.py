def solution(land):
    answer = 0
    col = len(land[0])
    row = len(land)
    visited = [[0] * col for _ in range(row)]
    result = [0] * col
    direc = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    for i in range(row):
        for j in range(col):
            if visited[i][j] or land[i][j] == 0:
                continue
            
            stack = [(i, j)]
            cols = set()
            total = 0
            
            while stack:
                r, c = stack.pop()
                
                if visited[r][c]:
                    continue
                
                total += 1
                cols.add(c)
                visited[r][c] = 1
                
                for x, y in direc:
                    nr = r + x
                    nc = c + y
                    
                    if not (0 <= nr < row) or not (0 <= nc < col):
                        continue
                        
                    if visited[nr][nc] or land[nr][nc] == 0:
                        continue
                    
                    stack.append((nr, nc))
            
            for k in cols:
                result[k] += total
    
    return max(result)