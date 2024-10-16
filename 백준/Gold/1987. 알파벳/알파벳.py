# 알파벳
import sys
input = sys.stdin.readline

r, c = map(int,input().split())

graph = []
for i in range(r):
    graph.append(input().rstrip())

maxx = 0
direc = [(0,1), (0,-1), (1,0), (-1,0)]
visited = [0] * 26

def dfs(x, y, cnt):
    global maxx

    maxx = max(maxx, cnt)
    
    for i in direc:
        new_x = x + i[0]
        new_y = y +i[1]
        
        if not(0 <= new_x < r) or not(0 <= new_y < c):
            continue

        char = ord(graph[new_x][new_y]) - ord("A")

        if visited[char]:
            continue

        visited[char] = 1
        dfs(new_x, new_y, cnt+1)
        visited[char] = 0
        
start = ord(graph[0][0]) - ord("A")
visited[start] = 1
dfs(0, 0, 1)
print(maxx) 
