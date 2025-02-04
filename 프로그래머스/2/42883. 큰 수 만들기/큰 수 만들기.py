def solution(number, k):
    answer = ""
    stack = [number[0]]
    for i in range(1, len(number)):
        while stack and k and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        
        stack.append(number[i])
    
    while k:
        stack.pop()
        k -= 1
        
    for i in stack:
        answer += i
        
    return answer