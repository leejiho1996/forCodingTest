def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0])) # 조건에 따라 정렬
    
    answer = 0
    for i in (data[row_begin-1]):
        answer += i % row_begin    
        
    for i in range(row_begin, row_end):
        tmp = 0
        for j in (data[i]):
            tmp += j % (i+1)
        answer = answer^tmp
        
    return answer