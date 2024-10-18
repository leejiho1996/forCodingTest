# 하늘에서 별똥별이 빗발친다
import sys
input = sys.stdin.readline

n, m, L, k = map(int,input().split())
stars = []
result = 0

for i in range(k):
    stars.append(tuple(map(int,input().split())))

for i in range(k):
    for j in range(k):
        row = stars[i][0] # 행의 기준
        col = stars[j][1] # 열의 기준 
        cnt = 0
        for h in range(k):
            nr, nc = stars[h][0], stars[h][1]

            if row <= nr <= row + L and col <= nc <= col + L:
                cnt += 1

        result = max(result, cnt)

print(k - result)
