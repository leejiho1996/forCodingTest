# 종이의 개수
import sys
input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

paper0 = 0
paper1 = 0
paper_minus = 0

def divide(row, col, num):
    global paper0
    global paper1
    global paper_minus

    if num == 0:
        return
    
    summ = []
    total = num*num
    for i in range(row, row+num):
        summ += board[i][col:col+num]

    if summ.count(-1) == total:
        paper_minus += 1
        return
    elif summ.count(1) == total:
        paper1 += 1
        return
    elif summ.count(0) == total:
        paper0 += 1
        return

    next_n = num // 3
    check = 0
    for i in range(0, 9):
        check = next_n*i
        next_row = row + (next_n * (check // num))
        next_col = col + check % num
        divide(next_row, next_col, next_n) 

divide(0,0,n)

print(paper_minus)
print(paper0)
print(paper1)
