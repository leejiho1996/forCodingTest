# 치킨 배달
import sys
input = sys.stdin.readline

def backtrack(limit, length, cnt):
    global result
    
    if cnt == m:
        total = 0
        for hr, hc in house:
            dist = 2500
            for cr, cc in chicken:
                if graph[cr][cc] == 2:
                    continue
                else:
                    dist = min(dist, abs(hr - cr) + abs(hc - cc))

            total += dist

        result = min(result, total)
            
        return 

    for i in range(limit, length):
        r, c = chicken[i]
        graph[r][c] = 0
        backtrack(i+1, length, cnt+1)
        graph[r][c] = 2

n, m = map(int,input().split())
graph = []
chicken = []
house = []
result = 650000

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 2:
            chicken.append((i, j))
        elif row[j] == 1:
            house.append((i, j))

backtrack(0, len(chicken), 0)
print(result)
