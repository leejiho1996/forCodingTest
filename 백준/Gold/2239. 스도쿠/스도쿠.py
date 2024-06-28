import sys
input = sys.stdin.readline

board = []
col = [[] for _ in range(9)]
zero = []

cnt = 0
for i in range(9):
    board.append(list(input().rstrip()))
    for j in range(9):
        col[j].append(board[i][j])
        if board[i][j] == '0':
            cnt += 1
            zero.append((i, j))

limit = len(zero)

def three(i ,j):
    row = i // 3 * 3
    col = j // 3 * 3
    three_list = []

    for i in range(row, row+3):
        for j in range(col, col+3):
            if board[i][j] != 0:
                three_list.append(board[i][j]) 
    return three_list

def backtrack(idx):
    if idx == limit:
        for i in board:
            print(*i,sep='')
        exit()
    
    x, y = zero[idx]
    three_list = three(x, y)

    for i in range(1, 10):
        if str(i) not in board[x] and str(i) not in col[y] and str(i) not in three_list:
            col[y][x] = str(i)
            board[x][y] = str(i)
            backtrack(idx+1)
            board[x][y] = '0'
            col[y][x] = '0'

backtrack(0)