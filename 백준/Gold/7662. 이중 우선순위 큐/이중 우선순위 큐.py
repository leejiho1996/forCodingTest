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
    dic = {}
    for j in range(k):
        cmd, num = input().rstrip().split()
        
        if cmd == "I":
            num = int(num)
            hq.heappush(min_heap, num)
            hq.heappush(max_heap, -num)
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            total += 1
            
        elif cmd == "D":
            if total == 0:
                continue
            
            if num == "-1":
                while not dic[min_heap[0]]:
                    hq.heappop(min_heap)
                dic[hq.heappop(min_heap)] -= 1
                    
            elif num == "1":
                while not dic[-max_heap[0]]:
                    hq.heappop(max_heap)
                dic[-hq.heappop(max_heap)] -= 1

            total -= 1
    
    if total == 0:
        print("EMPTY")
    else:
        while not dic[min_heap[0]]:
            hq.heappop(min_heap)
        while not dic[-max_heap[0]]:
            hq.heappop(max_heap)
        print(-hq.heappop(max_heap), hq.heappop(min_heap))
