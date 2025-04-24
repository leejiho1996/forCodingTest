# 낚시왕
import sys
input = sys.stdin.readline

R, C, M = map(int,input().split())
sharks = [0] * (R*C+1)
direc = {1:(-1, 0), 2:(1, 0), 3:(0, 1), 4:(0, -1)}
graph = [[0]*(C) for _ in range(R)]
result = 0

for i in range(M):
    r, c, s, d, z = map(int,input().split())
    r -= 1
    c -= 1
    graph[r][c] = (i+1)
    sharks[i+1] = [r, c, s, d, z]
    
for i in range(C):
    for j in range(R):
        if graph[j][i] != 0:
            result += sharks[graph[j][i]][4]
            sharks[graph[j][i]] = 0
            break

    tmp = [[0] * (C) for _ in range(R)]
    for j in range(1, R*C+1):
        if sharks[j] == 0:
            continue

        r, c, s, d, z = sharks[j]
        dx, dy = direc[d]
        nr = r + dx * s
        nc = c + dy * s
        nd = d
        
        if dx != 0:
            if nr < 0 or nr >= R:
                if nr <= 0:
                    nr = -nr

                if nr // (R-1) % 2 == 0:
                    nr = nr % (R-1)
                    nd = 2
                else:
                    nr = (R-1) - nr % (R-1)
                    nd = 1          
        elif dy != 0:
            if nc < 0 or nc >= C:
                if nc <= 0:
                    nc = -nc

                if nc // (C-1) % 2 == 0:
                    nc = nc % (C-1)
                    nd = 3
                else:
                    nc = (C-1) - nc % (C-1)
                    nd = 4

        sharks[j][0] = nr
        sharks[j][1] = nc
        sharks[j][3] = nd
        
        if tmp[nr][nc] != 0:

            if sharks[tmp[nr][nc]][4] > z:
                sharks[j] = 0
            else:
                sharks[tmp[nr][nc]] = 0
                tmp[nr][nc] = j
        else:
            tmp[nr][nc] = j

    graph = tmp

print(result)
