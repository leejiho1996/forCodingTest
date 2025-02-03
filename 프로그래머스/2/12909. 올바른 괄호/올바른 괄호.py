def solution(s):
    answer = True
    bracket = 0
    
    for cur in s:
        
        if cur == "(":
            bracket += 1
        else:
            bracket -= 1
        
        if bracket < 0:
            return False
    
    if bracket != 0:
        return False
    
    return True