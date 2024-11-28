def toBinary(n):
    result = ""
    while n > 1:
        result += str(n % 2)
        n //= 2
    
    result += str(n)
    
    return result[::-1]

def divide(n):
    stack = [n]
    
    while stack:
        cur = stack.pop()
            
        half = len(cur) // 2
        
        if cur[half] == "0":
            return 0
        
        right = cur[:half]
        left = cur[half+1:]
        
        if len(cur) > 3:
            if len(set(right)) > 1:
                stack.append(right)
            
            if len(set(left)) > 1:
                stack.append(left)
                
    return 1

def solution(numbers):
    answer = []
    
    for i in numbers:
        binary = toBinary(i)
        length = len(binary)
        n = 1
        
        while True:
            if 2**(n) - 1 < length:
                n += 1
            else:
                break
        
        binary = "0" * ((2**n - 1) - length) + binary
        
        answer.append(divide(binary))
    
    return answer