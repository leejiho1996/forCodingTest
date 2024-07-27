# 사회망 서비스
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
trees = [[] for _ in range(n+1)]

for i in range(n-1):
    u, v = map(int,input().split())
    trees[u].append(v)
    trees[v].append(u)

def dfs(n, prev):
    
    choice = 1
    non_choice = 0
    
    for i in (trees[n]):
        if i == prev:
            continue

        next_choice, next_non_choice = dfs(i, n)

        non_choice += next_choice # 현재 선택하지 않았다면 다음은 무조건 선택
        choice += min(next_choice, next_non_choice) # 선택했다면 작은값 선택
        
    return choice, non_choice

c, nc = dfs(1, -1)
print(min(c, nc))
