# 체스판 다시 칠하기 2
import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

dpB = [[0] * (m+1) for _ in range(n+1)]
dpW = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    board = input().rstrip()
    for j in range(1, m+1):
        if ((i+j) % 2 == 0 and board[j-1] == "B") or ((i+j) % 2 == 1 and board[j-1] == "W"):
            dpB[i][j] = dpB[i-1][j] + dpB[i][j-1] - dpB[i-1][j-1]
            dpW[i][j] = dpW[i-1][j] + dpW[i][j-1] - dpW[i-1][j-1] + 1
        else:
            dpB[i][j] = dpB[i-1][j] + dpB[i][j-1] - dpB[i-1][j-1] + 1
            dpW[i][j] = dpW[i-1][j] + dpW[i][j-1] - dpW[i-1][j-1] 

minn = 10000000000

for i in range(1, n-k+2):
    for j in range(1, m-k+2):
        checkB = dpB[i+k-1][j+k-1] - dpB[i-1][j+k-1] - dpB[i+k-1][j-1] + dpB[i-1][j-1]
        checkW = dpW[i+k-1][j+k-1] - dpW[i-1][j+k-1] - dpW[i+k-1][j-1] + dpW[i-1][j-1]
        minn = min(checkB, checkW, minn)

print(minn)
