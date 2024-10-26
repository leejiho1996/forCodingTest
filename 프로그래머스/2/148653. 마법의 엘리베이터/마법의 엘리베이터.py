def solution(storey):
    answer = 0
    
    while True:
        remainder = storey % 10 
        
        if remainder > 5: # 5보다 크면 더한다
            answer += (10 - remainder)
            storey += (10 - remainder)
        
        elif remainder == 5: # 5일경우 앞자리에 따라 나뉜다.
            five = storey // 10 % 10
            
            if five >= 5:
                storey += 5
            else:
                storey -= 5
            answer += 5
        
        else:
            answer += remainder # 5보다 작다면 빼준다
            storey -= remainder
        
        storey //= 10
        
        if storey == 0:
            break
            
    return answer