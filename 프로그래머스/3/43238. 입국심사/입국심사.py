def solution(n, times):
    answer = 0
    times.sort()
    start = 0 
    end = times[-1] * n    
    
    while start <= end:
        mid = (start + end) // 2
        people = 0
        
        for i in times:
            people += mid // i
        
        if people >= n:
            end = mid - 1
        else:
            start = mid + 1
        
    return end + 1