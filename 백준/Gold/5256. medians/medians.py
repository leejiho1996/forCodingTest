# medians
import sys
input = sys.stdin.readline
import heapq as hq

def popQue(limit, que):

    cnt = 0
    
    while cnt < limit:
        num = hq.heappop(que)
        num = abs(num)
        
        if visited[num]:
            continue
        else:
            visited[num] = 1
            result.append(num)

        cnt += 1

N = int(input())
B = list(map(int,input().split()))
visited = [0] * (2*N)
visited[B[0]] = 1

result = [B[0]]

minQue = []
maxQue = []

for i in range(2*N-1):
    hq.heappush(minQue, i+1)
    hq.heappush(maxQue, -(i+1))
    
for i in range(1, N):
    cur = B[i]

    if visited[cur]:
        limit = 2
    else:
        limit = 1
        result.append(cur)
        visited[cur] = 1
        
    if cur < B[i-1]:
        popQue(limit, minQue)        
    elif cur > B[i-1]:
        popQue(limit, maxQue)
    else:
        popQue(1, minQue)
        popQue(1, maxQue)

print(*result)
        
