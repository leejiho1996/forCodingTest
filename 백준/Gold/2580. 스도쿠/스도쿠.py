# 스도쿠
import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(9)]

row = [[0]*9 for _ in range(9)]
col = [[0]*9 for _ in range(9)]
square = [[0]*9 for _ in range(9)]
blank = []
          
for i in range(9):
    for j in range(9):
        number = board[i][j]
        if number:
            col[j][number-1] = 1
            row[i][number-1] = 1
            square[(i//3)* 3 + (j//3)][number-1] = 1
        else:
            blank.append([i,j])


def check(n):
    
    if n == len(blank):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end = ' ')
            print()
        exit()

    r, c = blank[n]

    for i in range(1, 10):
        if col[c][i-1] or row[r][i-1] or square[(r//3)* 3 + (c//3)][i-1]:
          continue
        else:
            board[r][c] = i
            col[c][i-1] = 1
            row[r][i-1] = 1
            square[(r//3)* 3 + (c//3)][i-1] = 1

            check(n+1)
            
            board[r][c] = 0
            col[c][i-1] = 0
            row[r][i-1] = 0
            square[(r//3)* 3 + (c//3)][i-1] = 0
            
check(0)
