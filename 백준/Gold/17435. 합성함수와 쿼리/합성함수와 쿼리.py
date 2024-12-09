# 합성함수 쿼리
import sys
input = sys.stdin.readline

m = int(input())
func = list(map(int,input().split()))
q = int(input())
maxx = 19
matrix = [[-1] * (m+1) for _ in range(maxx)]
matrix[0] = [0] + func

for i in range(1, maxx):
    for j in range(1, m+1):
        matrix[i][j] = matrix[i-1][matrix[i-1][j]]

for i in range(q):
    n, x = map(int,input().split())
    cur = x

    for i in range(maxx-1, -1, -1):
        if n & 1 << i:
            cur = matrix[i][cur]
    print(cur)