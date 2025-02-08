# A->B
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    que = deque([(a, 0)])

    while que:
        cur, cost = que.popleft()

        if cur == b:
            print(cost+1)
            return

        if cur in visited:
            continue
        else:
            visited.add(cur)

        if cur*2 <= b and cur*2 not in visited :
            que.append((cur*2, cost+1))

        plusOne = int(str(cur) + "1")
        
        if plusOne <= b and plusOne not in visited:
            que.append((plusOne, cost+1))

    print(-1)
    return

a, b = map(int,input().split())
visited = set()
bfs()