# 감시
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

cctv = {1:[(1,0,0,0), (-1,0,0,0), (0,-1,0,0), (0,1,0,0)],
        2:[(1,0,-1,0),(0,1,0,-1)],
        3:[(-1,-1,0,0), (-1,1,0,0), (1,-1,0,0), (1,1,0,0)],
        4:[(-1,-1,0,1), (1,1,-1,0), (1,1,0,-1), (-1,-1,1,0)],
        5:[(1,1,-1,-1)]
        }

graph = []
cctv_list = []
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] in cctv:
            cctv_list.append((row[j], i, j))
    graph.append(row)

def check(r, c, nr, nc, flag, mark):
    cur_r = r
    cur_c = c
    while nr:
        r += nr
        if not (0 <= r < n) or graph[r][cur_c] == 6:
            break

        if graph[r][cur_c] in cctv:
            continue

        if flag == 0 and graph[r][cur_c] != mark:
            continue

        if flag == mark and graph[r][cur_c] >= 100:
            continue
    
        graph[r][cur_c] = flag
    
    while nc:
        c += nc
        if not (0 <= c < m) or graph[cur_r][c] == 6:
            break
            
        if graph[cur_r][c] in cctv:
            continue
        
        if flag == 0 and graph[cur_r][c] != mark:
            continue

        if flag == mark and graph[cur_r][c] >= 100:
            continue

        graph[cur_r][c] = flag    

            
def dfs(cnt, limit):
    if cnt == limit:
        zero = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    zero += 1
        return zero

    cc, r, c = cctv_list[cnt]
    result = n*m

    for nr, nc, nr2, nc2 in cctv[cc]:
        check(r, c, nr, nc, 100+cnt, 100+cnt)
        check(r, c, nr2, nc2, 100+cnt, 100+cnt)
        result = min(result, dfs(cnt+1, limit))
        check(r, c, nr, nc, 0, 100+cnt)
        check(r, c, nr2, nc2, 0, 100+cnt)
            
    return result    

print(dfs(0, len(cctv_list)))
