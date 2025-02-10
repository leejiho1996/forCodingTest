# 파이프 옮기기1
import sys
input = sys.stdin.readline

def backtrack(i, j, pos):

    if i == n-1 and j == n-1: # 끝에 도착했다면 1을 리턴
        return 1

    if dp[pos][i][j] != -1:
        return dp[pos][i][j]
    else:
        dp[pos][i][j] = 0

    for dx, dy, nPos in dic[pos]:
        nx, ny = i + dx, j + dy
   
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        elif graph[nx][ny] == 1:
            continue

        if nPos == 2: # 대각선이동은 총 3칸을 확인해야함
            if graph[i+1][j] == 1 or graph[i][j+1] == 1:
                continue

        dp[pos][i][j] += backtrack(nx, ny, nPos)
        
    return dp[pos][i][j]

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    
dp = [[[-1] * n for _ in range(n)] for _ in range(3)]
dic = {0: [(0, 1, 0), (1, 1, 2)], 
       1:[(1, 0, 1), (1, 1, 2)],
       2:[(0,1, 0), (1, 0, 1), (1, 1, 2)]}

backtrack(0, 1, 0)

print(dp[0][0][1])
