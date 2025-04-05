# 트리
import sys
input = sys.stdin.readline

def dfs(n):
    global result
    
    check = False

    for i in childs[n]:
        if i == target:
            continue
        else:
            dfs(i)
            check = True

    if not check:
        result += 1

N = int(input())
childs = [[] for _ in range(N)]
start = 0
result = 0

parents = list(map(int,input().split()))
for i in range(N):
    if parents[i] == -1:
        start = i
        continue
    else:
        childs[parents[i]].append(i)

target = int(input())

if target == start:
    print(0)
else:
    dfs(start)
    print(result)
