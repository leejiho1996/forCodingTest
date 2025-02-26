# 배열 정렬
import sys
input = sys.stdin.readline
import heapq as hq

N = int(input())
array = list(map(int,input().split()))
sortedArr = tuple(sorted(array))
M = int(input())
visited = set()
commands = []

for i in range(M):
    l, r, c = map(int,input().split())
    commands.append((l, r, c))

que = []
hq.heappush(que,(0, tuple(array)))
while que:
    cost, cur = hq.heappop(que)

    if cur == sortedArr:
        print(cost)
        exit()
    
    if cur in visited:
        continue
    else:
        visited.add(cur)
    
    for l, r, c in commands:
        changed = list(cur)
        changed[l-1], changed[r-1] = changed[r-1], changed[l-1]
        changed = tuple(changed)

        if changed not in visited:
            hq.heappush(que, (cost + c, changed))
    
print(-1)
