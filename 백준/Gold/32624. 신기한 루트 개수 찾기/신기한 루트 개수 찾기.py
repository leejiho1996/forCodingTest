# 신기한 루트 갯수 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300001)

def dfs(cur):

    visited[cur] = 1
    cnt = 1
    child = 0
    
    for i in graph[cur]:

        if visited[i]:
            continue
        
        if i == B-1:
            child += 1
            continue

        nchild, ncnt = dfs(i)

        cnt += ncnt
        child += nchild
        
    return child, cnt

N, A, B = map(int,input().split())
visited = [0] * N
graph = [[] for _ in range(N)]

for i in range(N-1):
    n1, n2 = map(int,input().split())
    graph[n1-1].append(n2-1)
    graph[n2-1].append(n1-1)

visited[A-1] = 1

for i in graph[A-1]:
    if i == B-1:
        print(0)
        break
    
    child, cnt = dfs(i)

    if child:
        print(cnt)
        break
