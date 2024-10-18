# 불!
import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int,input().split())
direction = [(0,1), (0,-1), (1,0), (-1,0)]
j_que = deque()
f_que = deque()

graph = []
for i in range(r):
    row = list(input().rstrip())
    graph.append(row)
    
    for j in range(c):
        if row[j] == "J":
            j_que.append((i, j, 0))

        if row[j] == "F":
            f_que.append((i, j, 0))

time = 0
while f_que or j_que:
    while f_que and f_que[0][2] == time:
        x, y, t = f_que.popleft()
            
        for i in direction:
            new_x = x + i[0]
            new_y = y + i[1]
            if 0 <= new_x < r and 0 <= new_y < c:
                if graph[new_x][new_y] == "." or graph[new_x][new_y] == "J":
                    graph[new_x][new_y] = "F"
                    f_que.append((new_x, new_y, t+1))
                    
    while j_que and j_que[0][2] == time:
        x, y, t = j_que.popleft()

        if x== 0 or y == 0 or x == r - 1 or y == c -1:
            print(t+1)
            exit()
            
        for i in direction:
            new_x = x + i[0]
            new_y = y + i[1]
            if 0 <= new_x < r and 0 <= new_y < c:
                if graph[new_x][new_y] == ".":
                    graph[new_x][new_y] = "J"
                    j_que.append((new_x, new_y, t+1))

    time += 1

print("IMPOSSIBLE")
