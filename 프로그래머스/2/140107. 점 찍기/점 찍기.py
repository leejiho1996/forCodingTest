def solution(k, d):
    answer = 0
    
    check = d**2
    for i in range(0, d+1, k):
        possible = (check - i**2)**(0.5)
        answer += possible // k + 1
        
    return answer