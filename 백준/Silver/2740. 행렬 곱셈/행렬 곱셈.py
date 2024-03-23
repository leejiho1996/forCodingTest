# 행렬 곱셈
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int,input().split())))


n2, m2 = map(int, input().split())

b = [[] for _ in range(m2)]

for i in range(n2):
    matrix = list(map(int,input().split()))
    for j in range(m2):
        b[j].append(matrix[j])


result = [[] for _ in range(n)]

for i in range(n):
    for j in range(m2):
        cnt = 0
        for k in range(m):
            cnt +=a[i][k] * b[j][k]
        result[i].append(cnt)

for i in result:
    print(*i)