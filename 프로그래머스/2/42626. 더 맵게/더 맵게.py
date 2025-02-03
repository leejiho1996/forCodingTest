import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    
    while scoville:    
        if scoville[0] >= K:
            break
            
        if len(scoville) < 2:
            return -1
        
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        
        newOne = first + second*2
        hq.heappush(scoville, newOne)
        
        answer += 1
        
    return answer