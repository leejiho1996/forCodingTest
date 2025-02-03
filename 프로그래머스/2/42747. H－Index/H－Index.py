def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(citations[-1], -1, -1):
        cnt = 0
        for j in range(len(citations)-1, -1, -1):
            if citations[j] >= i:
                cnt += 1
            else:
                break
                
        if cnt >= i:
            return i
        
    return answer