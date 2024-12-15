# 프린터 큐
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    w = list(map(int,input().split()))
    works = []
    importance = []

    for j in range(n):
        work = w[j]
        works.append((j, work))
        importance.append(work)

    importance.sort()
    que = deque(works)
    cnt = 1
    
    while que:
        idx, num = que.popleft()
        if num < importance[-1]:
            que.append((idx, num))
        else:
            importance.pop()
            if idx == m:
                print(cnt)
                break
            cnt += 1
