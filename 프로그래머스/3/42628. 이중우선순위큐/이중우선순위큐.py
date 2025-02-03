import heapq as hq

def solution(operations):
    answer = []
    dic = {}
    minHeap = []
    maxHeap = []
    
    for i in operations:
        command, num = i.split(" ")
        num = int(num)

        if command == "I":
            hq.heappush(maxHeap, -num)
            hq.heappush(minHeap, num)
            
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
                
        elif command == "D" and num == 1:
            while maxHeap and dic[-maxHeap[0]] == 0: # 이미 제거된 숫자 제거
                hq.heappop(maxHeap)
                
            if maxHeap:
                num = -hq.heappop(maxHeap)
                dic[num] -= 1
                
        elif command == "D" and num == -1:
            while minHeap and dic[minHeap[0]] == 0: # 이미 제거된 숫자 제거
                hq.heappop(minHeap)
                
            if minHeap:
                num = hq.heappop(minHeap)
                dic[num] -= 1
    
    while maxHeap and dic[-maxHeap[0]] == 0: # 이미 제거된 숫자 제거
            hq.heappop(maxHeap)
    
    
    while minHeap and dic[minHeap[0]] == 0: # 이미 제거된 숫자 제거
            hq.heappop(minHeap)
    
    if not minHeap:
        return [0, 0]
    else:
        return [-maxHeap[0], minHeap[0]]
