import sys
input = sys.stdin.readline

h, w = map(int,input().split())
blocks = list(map(int,input().split()))

graph = [[0] * w for _ in range(h)]

for i in range(w):
    height = blocks[i]
    for j in range(height):
        graph[h-j-1][i] = 1

total = 0
for i in range(h):
    start = -1
    cnt = 0
    for j in range(w):
        if graph[i][j] == 1 and start == -1:
            start = j
        elif graph[i][j] == 1 and start != -1:
            cnt += j - start - 1
            start = j

    total += cnt

print(total)
