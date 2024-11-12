def solution(k, ranges):
    answer = []
    points = [k]
    areas = [0]
    
    while k != 1:
        if k % 2 == 0:
            k //= 2
        elif k % 2 == 1:
            k *= 3
            k += 1
            
        area = (k + points[-1]) / 2
        areas.append(areas[-1] + area)
            
        points.append(k)
    
    n = len(points) - 1
    
    for x, y in ranges:
        y = n + y
        
        if x > y or x > n:
            answer.append(-1)
        else:
            answer.append(areas[y] - areas[x])

    return answer