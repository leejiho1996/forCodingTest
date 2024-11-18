# 숫자 고르기
import sys
input = sys.stdin.readline

n = int(input())
down = []
visited = [0] * (n+1)

for i in range(n):
    down.append(int(input()))

def dfs(start, n):
    if visited[n]:
        return 0
    
    child = down[n-1]

    if start == child:
        return 1

    visited[n] = 1
    result = dfs(start, child)
    visited[n] = 0
    
    return result

result = []
    
for i in range(n):
    if dfs(i+1, i+1):
        result.append(i+1)

print(len(result))
for i in result:
    print(i)
