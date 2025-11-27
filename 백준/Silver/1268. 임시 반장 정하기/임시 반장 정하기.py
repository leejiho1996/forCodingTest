# 임시 반장 정하기
import sys
input = sys.stdin.readline

N = int(input())
graph = []
dic = {}

for i in range(N):
    row = list(map(int,input().split()))
    graph.append(row)

max_idx = 1
maxx = 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue

        for k in range(5):
            if graph[i][k] == graph[j][k]:
                cnt += 1
                break

    if cnt > maxx:
        maxx = cnt
        max_idx = i+1

print(max_idx)
