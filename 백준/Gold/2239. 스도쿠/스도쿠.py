import sys
input = sys.stdin.readline

board = []
col = [[0] * 10 for _ in range(9)]
three = [[0] * 10 for _ in range(9)] 
row = [[0] * 10 for _ in range(9)] 

for i in range(9):
    board.append(list(input().rstrip()))
    for j in range(9):
        num = int(board[i][j])
        col[j][num] = 1
        row[i][num] = 1

        three_idx = (i // 3 * 3) + (j // 3)
        three[three_idx][num] = 1

def backtrack(idx):
    if idx == 81:
        for i in board:
            print(*i,sep='')
        exit()
    
    x, y = idx // 9, idx % 9
    three_idx = (x // 3 * 3) + (y // 3)

    if board[x][y] != '0':
        backtrack(idx + 1)
    else:
        for i in range(1, 10):
            if not row[x][i] and not col[y][i] and not three[three_idx][i]:
                col[y][i] = 1
                row[x][i] = 1
                three[three_idx][i] = 1
                board[x][y] = str(i)
                backtrack(idx+1)
                col[y][i] = 0
                row[x][i] = 0
                three[three_idx][i] = 0
                board[x][y] = '0'

backtrack(0)