def solution(diffs, times, limit):
    answer = 0
    
    start = min(diffs)
    end = max(diffs)
    length = len(diffs) # 길이
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        
        for i in range(length):
            if i == 0:
                prev = 0 # 현재가 첫번째라면 prev 0
            else:
                prev = times[i-1] 
            
            cur = times[i]
            
            if mid >= diffs[i]:
                total += cur
            else:
                total += cur + ((diffs[i] - mid) * (prev + cur)) 
        
        if total > limit: # total > limit이면 level을 더 올려야함
            start = mid + 1
        else: # total <= limit 이면 level을 더 낮춰야함 
            end = mid - 1
        
    return start