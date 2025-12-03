# 특별히 큰 분수
import sys
input = sys.stdin.readline

x, N = map(int,input().split())

sett = {x}
cycle = [x]

while True:

    if x % 2 == 0:
        n = (x // 2) ^ 6
    else:
        n = (x * 2) ^ 6

    if n in sett:
        s_idx = cycle.index(n)
        break
    else:
        cycle.append(n)
        sett.add(n)

    x = n

if N <= s_idx:
    print(cycle[N])
else:
    N -= s_idx
    N %= len(cycle) - s_idx
    print(cycle[s_idx+N])
