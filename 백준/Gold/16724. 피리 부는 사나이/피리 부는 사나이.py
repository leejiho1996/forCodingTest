# 피리 부는 사나이
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
cnt = 0

graph = []
for i in range(n):
    graph.append(list(input().rstrip()))

direction = ("D","L","U","R")
dic = {"D":(1,0), "U":(-1,0), "L":(0,-1), "R":(0,1)}

def is_cycle(i, j, check):
    cycle = []
    row = i
    col = j
    while True:
        if graph[row][col] in direction:
            n_r, n_c = dic[graph[row][col]]
            graph[row][col] = str(check)
            row += n_r
            col += n_c
        elif graph[row][col] == str(check):
            return 1
        else:
            return 0
check = 0            
for i in range(n):
    for j in range(m):
        if graph[i][j] in direction:
            cnt += is_cycle(i, j, check)
        check += 1

print(cnt)
                
            