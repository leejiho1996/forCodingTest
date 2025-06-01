# 도로
import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])

    return parent[n]

N, M = map(int,input().split())
parent = [i for i in range(N)]
pos = []
resi = []
result = [0] * N

for i in range(N):
    row = input().rstrip()
    for j in range(N):
        if row[j] == "Y" and i < j:
            pos.append((i, j))

# 우선순위가 높은 도로부터 탐색하며 신장트리 만들기
link = 0
for x, y in pos:
    px = find(x)
    py = find(y)

    if px != py:
        parent[py] = px
        result[x] += 1
        result[y] += 1
        link += 1
    else:
        # 신장트리에 포함되지 않는 도로는 따로 저장
        resi.append((x, y))

if link < N-1 or len(resi) + link < M:
    print(-1)
else:
    for i in range(min(len(resi), (M - link))):
        x = resi[i][0]
        y = resi[i][1]
        result[x] += 1
        result[y] += 1

    print(*result)


