# 뱀
import sys
input = sys.stdin.readline
from collections import deque

n = int(input()); k = int(input())

graph = [[0] * n for _ in range(n)]
graph[0][0] = "S"

for i in range(k):
    x, y = map(int,input().split())
    graph[x-1][y-1] = "A"

l = int(input())

move = [0] * 10001
for i in range(l):
    t, p = input().rstrip().split()
    move[int(t)] = p

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
head = (0, 0)
tail = deque([])
snake_dir = direction[0]
cur = 0
cnt = 0

while True:
    h_x, h_y = head
    cnt += 1
    nHeadX = h_x + snake_dir[0]
    nHeadY = h_y + snake_dir[1]       
    tail.append((h_x, h_y))

    if not (0 <= nHeadX < n) or not (0 <= nHeadY < n) or graph[nHeadX][nHeadY] == "S": 
        break
 
    if cnt <= 10000 and move[cnt] != 0:
        direc = move[cnt]
        if direc == "L":
            cur -= 1
        else:
            cur += 1
        snake_dir = direction[(cur) % 4]

    if graph[nHeadX][nHeadY] == "A":
        head = (nHeadX, nHeadY)
        graph[nHeadX][nHeadY] = "S"
        continue

    head = (nHeadX, nHeadY)
    graph[nHeadX][nHeadY] = "S"
    
    t_x, t_y = tail.popleft()
    graph[t_x][t_y] = 0
                    
print(cnt)
