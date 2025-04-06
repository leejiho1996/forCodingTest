# 배
import sys
input = sys.stdin.readline

def find(n):
    if parent[n] < 0:
        return parent[n]
    
    if parent[n] != n:
        parent[n] = find(parent[n])

    return parent[n]

N = int(input())
crane = list(map(int,input().split()))

M = int(input())
pears = list(map(int,input().split()))

crane.sort()
pears.sort()

parent = [i for i in range(M)]
cnt = 0
time = 0

if crane[-1] < pears[-1]:
    print(-1)
    exit()

while cnt < M:
    for i in range(N):
        cur = crane[i]
        start = 0
        end = M-1
        
        while start <= end:

            mid = (start + end) // 2

            if cur >= pears[mid]:
                start = mid + 1
            else:
                end = mid - 1

        p = find(start-1)

        if p < 0 or pears[p] > cur:
            continue
        
        if p == 0:
            parent[p] = -1
            cnt += 1
        elif p > 0:
            parent[p] = find(p-1)
            cnt += 1
            
    time += 1

print(time)
