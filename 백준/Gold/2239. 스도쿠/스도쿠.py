import sys
input = sys.stdin.readline

board = []
col = [[] for _ in range(9)]
zero = []
three = [[0] * 10 for _ in range(9)] 

for i in range(9):
    board.append(list(input().rstrip()))
    for j in range(9):
        col[j].append(board[i][j])
        if board[i][j] == '0':
            zero.append((i, j))
        three_idx = (i // 3 * 3) + (j // 3)

        three[three_idx][int(board[i][j])] = 1

limit = len(zero)


def backtrack(idx):
    if idx == limit:
        for i in board:
            print(*i,sep='')
        exit()
    
    x, y = zero[idx]
    three_idx = (x // 3 * 3) + (y // 3)


    for i in range(1, 10):
        if str(i) not in board[x] and str(i) not in col[y] and str(i) and three[three_idx][i] != 1:
            col[y][x] = str(i)
            board[x][y] = str(i)
            three[three_idx][i] = 1
            backtrack(idx+1)
            board[x][y] = '0'
            col[y][x] = '0'
            three[three_idx][i] = 0

backtrack(0)


