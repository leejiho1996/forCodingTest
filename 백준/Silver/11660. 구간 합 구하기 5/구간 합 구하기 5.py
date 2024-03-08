# 구간 합 구하기 5
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
table = [[0] * (n+1) for _ in range(n)] 


for i in range(n):
    s = 0
    for j, n in enumerate(list(map(int,input().split()))):
        s += n 
        table[i][j+1] = s
        
for i in range(m):
    s_row, s_col, e_row, e_col = map(int,input().split())

    s = 0
    for j in range(s_row-1, e_row):
        s += table[j][e_col] - table[j][s_col-1]        

    print(s)