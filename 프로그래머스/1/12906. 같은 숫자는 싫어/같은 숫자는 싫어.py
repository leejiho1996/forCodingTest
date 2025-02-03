def solution(arr):
    answer = []
    last = arr[-1]
    
    while arr and arr[-1] == last:
        cur = arr.pop()
        
        if not arr:
            answer.append(cur)
            
        elif arr[-1] != last:
            last = arr[-1]
            answer.append(cur)
        
    return answer[::-1]