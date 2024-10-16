# 경사로
import sys
input = sys.stdin.readline

n, L = map(int,input().split())

graph = []
col = []

for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    e = []
    for j in range(n):
        e.append(graph[j][i])
    col.append(e)
    
cnt = n*2

def check(side):
    if side == 0:
        g = graph
    else:
        g = col

    cnt = n
    visited = [[0] * n for _ in range(n)]
    
    for i in range(n):
        cur = 0
        while True:
            if cur >= n-1:
                break
            
            head = g[i][cur]
            nextt = g[i][cur+1]
            possible = True
            
            if abs(head - nextt) > 1 : # 해당 길은 이동 불가
                possible = False
                break

            
            
            if head - nextt == 1: # 선도 블럭이 더 큰경우
                if cur + L >= n:
                    break

                for j in range(cur+1, cur+L+1):
                    if nextt != g[i][j] or visited[i][j]:
                        possible = False
                        break
                    
                if possible:
                    for j in range(cur+1, cur+L+1):
                        visited[i][j] = 1
                    cur += L-1

            elif head - nextt == -1: # 선도 블럭이 더 작은 경우
                if cur - L + 1 < 0:
                    break
                
                for j in range(cur-L+1, cur+1):
                    if head != g[i][j] or visited[i][j]:
                        possible = False
                        break
                    
                if possible:
                    for j in range(cur-L+1, cur+1):
                        visited[i][j] = 1

            if possible:
                cur += 1
            else:
                break
           
        if cur != n-1:
            cnt -= 1

    return cnt

row_cnt = check(0)
col_cnt = check(1)
print(row_cnt + col_cnt)
