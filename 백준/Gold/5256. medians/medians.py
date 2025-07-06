# medians
import sys
input = sys.stdin.readline

def find(limit, idx, flag):

    cnt = 0
    
    while cnt < limit:
        num = nums[idx]

        if visited[num]:
            idx += flag
            continue
        else:
            result.append(num)
            visited[num] = 1
            idx += flag
            cnt += 1

    return idx

N = int(input())
B = list(map(int,input().split()))
visited = [0] * (2*N)
visited[B[0]] = 1
nums = [i for i in range(2*N)]

result = [B[0]]
minIdx = 1
maxIdx = 2*N-1

for i in range(1, N):
    cur = B[i]

    if visited[cur]:
        limit = 2
    else:
        limit = 1
        result.append(cur)
        visited[cur] = 1
        
    if cur < B[i-1]:
        minIdx = find(limit, minIdx, 1)        
    elif cur > B[i-1]:
        maxIdx = find(limit, maxIdx, -1)
    else:
        minIdx = find(1, minIdx, 1)
        maxIdx = find(1, maxIdx, -1)

print(*result)
        
