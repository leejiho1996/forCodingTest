def solution(prices):
    length = len(prices)
    prices[-1] = 0
    answer = [0] * length
    stack = []
    
    for i in range(length):
        while stack and stack[-1][1] > prices[i]:
            idx, num = stack.pop()
            answer[idx] = i - idx
            
        stack.append((i, prices[i]))
        
    return answer