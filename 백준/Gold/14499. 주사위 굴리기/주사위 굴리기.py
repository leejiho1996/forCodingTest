# 주사위 굴리기
import sys
input = sys.stdin.readline

n, m, x, y, k = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

d1, d2, d3, d4, d5, d6 = 0, 0, 0, 0, 0, 0

direc = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}

dice_x, dice_y = x, y

seq = list(map(int,input().split()))

for i in range(k):
    x, y = direc[seq[i]]
    next_x = dice_x + x
    next_y = dice_y + y

    if not (0 <= next_x < n) or not (0 <= next_y < m):
        continue

    if seq[i] == 1:
        d1, d2, d3, d4, d5, d6 = d1, d6, d2, d3, d5, d4
    elif seq[i] == 2:
        d1, d2, d3, d4, d5, d6 = d1, d3, d4, d6, d5, d2 
    elif seq[i] == 3:
        d1, d2, d3, d4, d5, d6 = d3, d2, d5, d4, d6, d1 
    else:
        d1, d2, d3, d4, d5, d6 = d6, d2, d1, d4, d3, d5

    print(d3)

    if graph[next_x][next_y] == 0:
        graph[next_x][next_y] = d6
    else:
        d6 = graph[next_x][next_y]
        graph[next_x][next_y] = 0

    dice_x = next_x
    dice_y = next_y
  