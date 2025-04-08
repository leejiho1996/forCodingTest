# 저울
import sys
input = sys.stdin.readline

def search(arrlist, root, n):
    global cnt
    
    visited[n] = True

    if root != n:
        cnt += 1

    for i in arrlist[n]:
        if visited[i] == 0:
            search(arrlist, root, i)
            
N = int(input())
M = int(input())

front = [[] for _ in range(N+1)]
back = [[] for _ in range(N+1)]

for i in range(M):
    f, b = map(int,input().split())
    front[b].append(f)
    back[f].append(b)

for i in range(1, N+1):
    visited = [0] * (N+1)
    cnt = 1
    search(front, i, i)
    search(back, i, i)
    print(N-cnt)
