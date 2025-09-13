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
        
        if i == B:
            child += 1 # B와 이어진 노드라면 체크
            continue

        nchild, ncnt = dfs(i)

        cnt += ncnt
        child += nchild
        
    return child, cnt

N, A, B = map(int,input().split())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited[A] = 1
for i in graph[A]:
    if i == B: # A와 B가 인접 노드라면 LCA가 A, B 밖에 안되므로 0 출력
        print(0)
        break
    
    child, cnt = dfs(i)

    if child: # 만약 B와 연결된 노드를 탐색했다면 카운트 출력후 종료
        print(cnt)
        break
