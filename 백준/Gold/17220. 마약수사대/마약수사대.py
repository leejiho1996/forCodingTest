# 마약수사대
import sys
input = sys.stdin.readline

def dfs(n):

    visited[n] = 1
    
    for i in graph[n]:
        if not visited[i] and i not in remove:
            dfs(i)

dic = {}

for i in range(26):
    dic[chr(65+i)] = i

N, M = map(int,input().split())

front = [0] * N
graph = [[] for _ in range(N)]
visited = [0] * N
remove = set()
cnt = 0

for i in range(M):
    s, t = input().rstrip().split()
    graph[dic[s]].append(dic[t])
    front[dic[t]] += 1

tmp = set(input().rstrip().split()[1:])

for i in tmp:
    remove.add(dic[i])

for i in range(N):
    if front[i] == 0 and i not in remove:
        dfs(i)
        cnt += 1

print(sum(visited) - cnt)
