from collections import deque

def solution(board):
    row = len(board)
    col = len(board[0])
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == "R":
                r_row = i
                r_col = j
                break
                
    que = deque([(r_row, r_col, 0)])
    visit = [[-1]*col for _ in range(row)]
    
    while que:
             
        cur_row, cur_col, n = que.popleft()
        
        if board[cur_row][cur_col] == "G":
            return n
        
        for dr, dc in ((1,0), (-1,0), (0,-1), (0,1)): # 상하좌우
            if (0<= cur_row + dr < row and 0<= cur_col + dc < col and board[cur_row + dr][cur_col+dc] != "D"):
                r = cur_row
                c = cur_col
                while True:
                    r += dr
                    c += dc
                    if r == -1 or r == row or c == -1 or c == col or board[r][c] == "D":
                        if visit[r-dr][c-dc] == -1:
                            que.append((r-dr, c-dc, n+1))
                            visit[r-dr][c-dc] = 0
                            break
                        else:
                            break
    return -1