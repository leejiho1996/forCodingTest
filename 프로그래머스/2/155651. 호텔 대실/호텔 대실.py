def solution(book_time):
    answer = 0
    length = len(book_time) # 주어진 시간 길이
    time = [0] * ((60 * 24)+9) # 총 시간 (분단위)
    
    for i in range(length):
        start, end = book_time[i]
        start_hour, start_minute = map(int, start.split(":"))
        end_hour, end_minute = map(int, end.split(":"))
        end_minute += 9 # 청소시간 9분 더해준다 (10분 후 부터는 사용 가능)
        
        s_minute = start_hour * 60 + start_minute
        e_minute = end_hour * 60 + end_minute
        
        for i in range(s_minute, e_minute+1):
            time[i] += 1
    
    answer = max(time)
                                 
    return answer