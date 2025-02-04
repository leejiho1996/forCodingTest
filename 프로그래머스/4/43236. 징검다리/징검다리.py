def solution(distance, rocks, n):
    length = len(rocks)
    rocks.sort()
    between = [0] * (length + 1)
    between[0] = rocks[0]
    between[-1] = distance - rocks[-1]
    
    for i in range(length-1):
        between[i+1] = rocks[i+1] - rocks[i]
    
    start = 0
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0 # 제거할 돌 카운트 
        dist = 0 # 돌 사이 간격
        
        for i in between:
            dist += i
            
            if dist < mid:
                cnt += 1
            else:
                dist = 0
        
        if n >= cnt:
            start = mid + 1
        else:
            end = mid - 1
    
    return start - 1