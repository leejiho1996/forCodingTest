# 틱택토
import sys
input = sys.stdin.readline

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

while True:
    string = input().rstrip()
    if string == 'end':
        break
    
    board = [[0, 0, 0] for _ in range(3)]
    o_cnt = 0
    x_cnt = 0
    
    for i in range(9):
        row = i // 3
        col = i % 3
        board[row][col] = string[i]

        if string[i] == "O":
            o_cnt +=1
        elif string[i] == "X":
            x_cnt += 1

    oe, ox = straight(board)

    if (not ox and not oe) and o_cnt + x_cnt < 9: # 완성된 경우가 없는데 빈칸이 있는 경우
        print("invalid")
        continue

    if oe and ox: # 둘다 3개가 완성되는 경우가 있을 수 없음
        print("invalid") 
        continue
    
    if x_cnt < o_cnt: # o가 후공이라서 더 많을 수 없음
        print("invalid") 
        continue

    if x_cnt - o_cnt > 1: # x가 o보다 1개 이상 많을 수 없음
        print("invalid") 
        continue

    if o_cnt == x_cnt and ox:  # o, x의 수가 같은데 x가 완성될수 없음
        print("invalid") 
        continue

    if o_cnt < x_cnt and oe: # x수가 더 많은데 o가 완성 될 수 없음
        print("invalid") 
        continue

    print("valid")
    
