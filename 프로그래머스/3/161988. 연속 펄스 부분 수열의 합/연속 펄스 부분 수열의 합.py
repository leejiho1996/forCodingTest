def solution(sequence):
    
    dp1 = [sequence[0]]
    dp2 = [sequence[0] * -1]
    
    for i in range(1, len(sequence)):
        if i % 2 == 1:
            pulse = -1
        else:
            pulse = 1
            
        dp1.append(max(dp1[i-1] + sequence[i] * pulse, sequence[i] * pulse))  
        dp2.append(max(dp2[i-1] + sequence[i] * (-pulse), sequence[i] * (-pulse)))
        
    return max(max(dp1), max(dp2))