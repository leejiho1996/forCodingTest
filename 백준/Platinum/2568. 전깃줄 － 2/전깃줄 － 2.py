# 전깃줄-2
import sys
input = sys.stdin.readline

n = int(input())
links = []
seq = [1 for _ in range(n)]
visited = [0] * n

for i in range(n):
    s, t = map(int,input().split())
    links.append((s,t))

links.sort()

lcs = [links[0][1]]

for i in range(1, n):
    cur = links[i][1]
    
    if lcs[-1] < cur:
        lcs.append(cur)
        seq[i] = len(lcs)
        continue

    start = 0
    end = len(lcs) - 1

    while start <= end:
        mid = (start + end) // 2

        if lcs[mid] >= cur:
            end = mid - 1
        else:
            start = mid + 1
    
    lcs[end+1] = cur   
    seq[i] = end+2

cnt = len(lcs)
for i in range(n-1, -1, -1):
    if seq[i] == cnt:
        cnt -= 1
        visited[i] = 1

    if cnt == 0:
        break

print(n - len(lcs))
for i in range(n):
    if visited[i] == 0:
        print(links[i][0])
