def solution(k, tangerine):
    tan = []
    dic = {}
    answer = 0
    
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    for i in dic.keys():
        tan.append(dic[i])
    
    tan.sort(reverse=True)
    
    for i in tan:
        if k - i <= 0:
            answer += 1
            break
        else:
            k -= i
            answer += 1
            
    return answer