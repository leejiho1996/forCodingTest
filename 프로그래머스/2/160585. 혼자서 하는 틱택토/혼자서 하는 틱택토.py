def straight(board):
    xe = False
    oe = False
    cross1 = ""
    cross2 = ""
    for i in range(3):
        row = ""
        col = ""
        cross1 += board[i][i]
        cross2 += board[2-i][i]
        for j in range(3):
            row += board[i][j]
            col += board[j][i]
        if row == "XXX" or col == "XXX" or cross1 =="XXX" or cross2 == "XXX":
            xe = True            
        
        if row == "OOO" or col == "OOO" or cross1 == "OOO" or cross2 == "OOO":
            oe = True
    
    return (oe, xe)

def solution(board):
    answer = 1
    o_cnt = 0
    x_cnt = 0
    
    o = []
    x = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o.append((i,j))
                o_cnt += 1
            elif board[i][j] == "X":
                x.append((i,j))
                x_cnt += 1
    
    oe, ox = straight(board)
    
    if oe and ox: # 둘다 3개가 완성되는 경우가 있을 수 없음
        return 0 
    
    if x_cnt > o_cnt: # x가 후공이라서 더 많을 수 없음
        return 0
    
    if o_cnt - x_cnt > 1: # o가 x보다 1개 이상 많을 수 없음
        return 0
    
    if o_cnt == x_cnt and oe:  # o, x의 수가 같은데 o가 완성될수 없음
        return 0
    
    if o_cnt > x_cnt and ox: # 위 조건들에 해당이 안된다면 o가 1개 많은 경우 그런데 x가 완성되어있다면 불가능
        return 0
    
    
    return answer