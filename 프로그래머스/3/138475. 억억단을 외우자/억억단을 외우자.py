def solution(e, starts):
    answer = []
    yaksu = [2] * (e + 1)
    yaksu[1] -= 1
    
    for i in range(2, e+1):
        start = i*2
        
        while start <= e:
            yaksu[start] += 1
            start += i
    
    result = [0] * (e + 1)
    
    maxx = 0
    cnt = 0
    for i in range(e, 0, -1):
        if cnt <= yaksu[i]:
            cnt = yaksu[i]
            maxx = i
            
        result[i] = maxx
    
    for i in starts:
        answer.append(result[i])
    
    return answer