def solution(brown, yellow):
    answer = []
    
    for i in range(1, int(yellow**(0.5))+1):
        if yellow % i != 0:
            continue    
        height, width = i, yellow//i
        
        possible = 2 * (width + height + 2)
        
        if possible == brown:
            return [width+2, height+2]
        
    return answer