# 이중 우선순위 큐
import sys
input = sys.stdin.readline
import heapq as hq

t = int(input())

for i in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    total = 0
    visited = [0] * 1000001
    for j in range(k):
        cmd, num = input().rstrip().split()
        
        if cmd == "I":
            num = int(num)
            hq.heappush(min_heap, (num, j))
            hq.heappush(max_heap, (-num, j))
            visited[j] = 1
            total += 1
            
        elif cmd == "D":
            if total == 0:
                continue
            
            if num == "-1":
                while not visited[min_heap[0][1]]:
                    hq.heappop(min_heap)
                visited[hq.heappop(min_heap)[1]] = 0
                    
            elif num == "1":
                while not visited[max_heap[0][1]]:
                    hq.heappop(max_heap)
                visited[hq.heappop(max_heap)[1]] = 0

            total -= 1

            if total == 0:
                min_heap = []
                max_heap = []
    
    if total == 0:
        print("EMPTY")
    else:
        while not visited[min_heap[0][1]]:
            hq.heappop(min_heap)
        while not visited[max_heap[0][1]]:
            hq.heappop(max_heap)
        print(-hq.heappop(max_heap)[0], hq.heappop(min_heap)[0])
