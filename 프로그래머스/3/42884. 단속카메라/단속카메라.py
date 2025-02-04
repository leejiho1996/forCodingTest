def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[0])

    tail = -30001
    cnt = 0
    for i in routes:
        start = i[0]
        end = i[1] 
        
        if tail >= start:
            tail = min(tail, end)
            continue
        else:
            tail = end
            cnt += 1
            
    return cnt