# 선발 명단
import sys
input = sys.stdin.readline

def backtrack(cur, score):
    global result
    
    if cur == 11:
        result = max(result, score)
        return

    for i in range(11):
        if graph[cur][i] == 0 or visited[i]:
            continue

        visited[i] = 1
        backtrack(cur+1, score + graph[cur][i])
        visited[i] = 0
    
C = int(input())

for _ in range(C):
    visited = [0] * 11
    graph = []
    result = 0

    for j in range(11):
        graph.append(list(map(int,input().split())))

    backtrack(0, 0)

    print(result)
