# 알파벳
import sys
input = sys.stdin.readline

r, c = map(int,input().split())

graph = []
for i in range(r):
    graph.append(input().rstrip())

maxx = 0
direc = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(x, y, cnt, alphabet):
    global maxx

    maxx = max(maxx, cnt)
    
    for i in direc:
        new_x = x + i[0]
        new_y = y +i[1]

        if not(0 <= new_x < r) or not(0 <= new_y < c) or graph[new_x][new_y] in alphabet:
            continue

        new_alphabet = alphabet+graph[new_x][new_y]
    
        dfs(new_x, new_y, cnt+1, new_alphabet)

start = graph[0][0]

dfs(0, 0, 1, start)
print(maxx) 