def solution(points, routes):
    answer = 0
    sett = set()
    result = set()
    robots = len(routes)
    
    for i in range(robots):
        start = routes[i][0] - 1
        cur_routes = len(routes[i])
        cnt = 0
        start_r = points[start][0] # 시작 row
        start_c = points[start][1] # 시작 col
        
        if (start_r, start_c, cnt) not in sett:
            sett.add((start_r, start_c, cnt))
        else:
            result.add((start_r, start_c, cnt))
        
        for k in range(1, cur_routes):
            to = routes[i][k] - 1
            to_r = points[to][0] # 도착 row
            to_c = points[to][1] # 도착 col

            if to_r > start_r:
                sign = 1
            else:
                sign = -1

            for j in range(abs(to_r - start_r)):
                cnt += 1
                start_r += sign

                if (start_r, start_c, cnt) not in sett:
                    sett.add((start_r, start_c, cnt))
                else:
                    result.add((start_r, start_c, cnt))

            if to_c > start_c:
                sign = 1
            else:
                sign = -1

            for j in range(abs(to_c - start_c)):
                cnt += 1
                start_c += sign

                if (start_r, start_c, cnt) not in sett:
                    sett.add((start_r, start_c, cnt))
                else:
                    result.add((start_r, start_c, cnt))
                    
    return len(result)