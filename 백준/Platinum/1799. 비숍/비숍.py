# 비숍
import sys
input = sys.stdin.readline

def backtrack(cnt, total, color):
    global result

    result[color] = max(result[color], total)

    if cnt >= N*2-1:
        return

    sr = max(cnt-(N-1), 0)
    sc = min(cnt, N-1)
    
    iterCnt = min(2*N-(cnt+1), cnt+1) # 반복 횟수

    check = False
    for i in range(iterCnt):
        rightDist = abs(0 - (sr+i)) + abs(N-1 - (sc-i))

        if graph[sr+i][sc-i] == 0 or right[rightDist] == 1:
            continue
        
        check = True
        right[rightDist] = 1
        backtrack(cnt+2, total+1, color)
        right[rightDist] = 0

    if not check:
        backtrack(cnt+2, total, color)
        
N = int(input())
graph = []
left = [0] * (N*2 - 1)
right = [0] * (N*2 - 1)
result = [0, 0]

for i in range(N):
    row = list(map(int,input().split()))
    graph.append(row)

    for j in range(N):
        if row[j] == 1:
            left[abs(0 - i) + abs(0 - j)] = 1
    
backtrack(0, 0, 0)
backtrack(1, 0, 1)
print(result[0] + result[1])
