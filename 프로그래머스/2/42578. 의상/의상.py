def solution(clothes):
    answer = 1
    dic = {}
    
    for i in clothes:
        wear = i[0]
        types = i[1]
        
        if types not in dic:
            dic[types] = 1
        else:
            dic[types] += 1
        
    
    for i in dic.keys():
        answer *= dic[i] + 1
        
    return answer - 1