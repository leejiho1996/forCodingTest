def solution(n, l, r):
    answer = 0
    
    check = 5**(n-1)
    
    for i in range(l-1, r):
        cur = i
        if i // check == 2:
            continue
            
        while i > 5:
            if i % 5 == 2:
                break
    
            i //= 5
            
        if i % 5 != 2:
            answer += 1
    
    return answer