# 연결 요소의 개수
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

link = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def dfs(node):
    stack = []
    for i in link[node]:
        stack.append(i)

    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        else:
            visited[cur] = 1

        for j in link[cur]:
            if visited[j]:
                continue
            else:
                stack.append(j)

for i in range(m):
    start, to = map(int,input().split())
    link[start].append(to)
    link[to].append(start)

cnt = 0
for i in range(1, n+1):
    if visited[i]:
        continue
    else:
        visited[i] = 1
        cnt += 1
        dfs(i)
        
print(cnt)
