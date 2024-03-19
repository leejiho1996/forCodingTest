# 테트로미노
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

tet = [list(map(int, input().split())) for _ in range(n)]

maxx = 0

def search(x, y, cnt, total):
    global maxx
    if tet[x][y]:
        total += tet[x][y]
        tmp = tet[x][y]
        tet[x][y] = False
    else:
        return
    
    if cnt == 4:
        maxx = max(maxx, total)
        tet[x][y] = tmp
        return
  
    for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
        if 0 <= (x+dx) < n and 0 <= (y+dy) < m:
            search(x+dx, y+dy, cnt+1, total)

    tet[x][y] = tmp
            
    

for i in range(n):
    for j in range(m):
        t_count = 0
        t_sum = tet[i][j]
        t_min = 1001
        for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
            if 0 <= (i+dx) < n and 0 <= (j+dy) < m:
                t_count += 1
                t_sum += tet[i+dx][j+dy]
                t_min = min(t_min, tet[i+dx][j+dy])
        if t_count == 4:
            t_sum -= t_min
        maxx = max(t_sum, maxx)
                
        search(i,j,1,0)

print(maxx)
