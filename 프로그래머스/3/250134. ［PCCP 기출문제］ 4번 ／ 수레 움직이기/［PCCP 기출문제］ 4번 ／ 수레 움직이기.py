from collections import deque

def solution(maze):
    row = len(maze)
    col = len(maze[0])
    visited_red = 1 << (row * col + 1)
    visited_blue = 1 << (row * col + 1)
    direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in range(row):
        for j in range(col):
            if maze[i][j] == 5:
                visited_red |= 1 << (i * col + j + 1)
                visited_blue |= 1 << (i * col + j + 1)
            
            if maze[i][j] == 1:
                red_start = (i, j)
                visited_red |= 1 << (i * col + j + 1)
                
            if maze[i][j] == 2:
                blue_start = (i, j)
                visited_blue |= 1 << (i * col + j + 1)
            
            if maze[i][j] == 3:
                red_end = (i, j)
            
            if maze[i][j] == 4:
                blue_end = (i, j)
        
    pos = deque([(red_start[0], red_start[1], blue_start[0], blue_start[1], visited_red, visited_blue , 0)])
    
    while pos:
        rr, rc, br, bc, vr, vb, cnt = pos.popleft()
        
        if (rr, rc) == red_end and (br, bc) == blue_end:
            return cnt
        
        for rx, ry in direc:
                    
            if (rr, rc) == red_end:
                nrr, nrc = rr, rc
            else:
                nrr, nrc = rr + rx, rc + ry
            
            if not (0 <= nrr < row) or not (0 <= nrc < col):
                continue
            
            red_next = 1 << (nrr * col + nrc + 1)
            
            if (rr, rc) != red_end and vr & red_next:
                continue

            for bx, by in direc:
                    
                if (br, bc) == blue_end:
                    nbr, nbc = br, bc
                else:
                    nbr, nbc = br + bx, bc + by
                    
                if not (0 <= nbr < row) or not (0 <= nbc < col) or (nrr == nbr and nrc == nbc):
                    continue
                    
                blue_next = 1 << (nbr * col + nbc + 1)
                
                if (br, bc) != blue_end and vb & blue_next:
                    continue
                
                if (nrr == br and nrc == bc and nbr == rr and nbc == rc):
                    continue
                    
                pos.append((nrr, nrc, nbr, nbc, vr | red_next, vb | blue_next, cnt+1))

    return 0