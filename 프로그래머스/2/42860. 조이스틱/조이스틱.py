def solution(name):
    dic = {}
    answer = 0
    for i in range(26):
        dic[chr(65+i)] = i+1
    
    change = []
    upDown = 0
    leftRight = len(name) - 1
    
    for i in range(len(name)):
        upDown += min(abs(dic[name[i]] - 1), 1 + (26 - dic[name[i]]))
        if i != 0:
            change.append(i)
    
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1   
        leftRight = min(leftRight, 2 * i + len(name) - next, i + 2 * (len(name) - next))
        
    return upDown + leftRight