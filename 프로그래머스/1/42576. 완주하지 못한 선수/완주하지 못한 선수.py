def solution(participant, completion):

    dic = {}
    
    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for i in completion:
        dic[i] -= 1
    
    for i in participant:
        if dic[i] != 0:
            return i
    
