def solution(sequence):
    
    start_plus = sequence.copy()
    start_minus = sequence.copy()
    length = len(sequence)
    mul = 1
    
    for i in range(length):
        start_plus[i] *= mul
        start_minus[i] *= -mul
        mul = -mul
        
    plus = 0
    minus = 0
    max_plus = start_plus[0]
    max_minus = start_minus[0]
    
    for i in range(length):
        plus += start_plus[i]
        max_plus = max(max_plus, plus)
        if plus < 0:
            plus = 0
        
        minus += start_minus[i]
        max_minus = max(max_minus, minus)
        if minus < 0:
            minus = 0
    
    return max(max_plus, max_minus)