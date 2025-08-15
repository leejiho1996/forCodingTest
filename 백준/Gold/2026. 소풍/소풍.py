# 소풍
import sys
input = sys.stdin.readline

def backtrack(cur, friends, cnt):

    if cnt == K:
        for i in result:
            print(i)
        exit()
        
    for i in range(cur+1, N+1):
        if friends[i] == 0:
            continue

        new_friends = [0] * (N+1)
        count = 0
        
        for j in range(1, N+1):
             if friends[j] == 1 and graph[i][j] == 1:
                 count += 1
                 new_friends[j] = 1

        if count >= K:
            result.append(i)
            backtrack(i, new_friends, cnt+1)
            result.pop()
    
K, N, F = map(int,input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
result = []

for i in range(1, N+1):
    graph[i][i] = 1

for i in range(F):
    n1, n2 = map(int,input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1
        
for i in range(1, N+1):
    result.append(i)
    backtrack(i, graph[i].copy(), 1)
    result.pop()

print(-1)
