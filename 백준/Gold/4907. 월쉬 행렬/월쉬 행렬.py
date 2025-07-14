# 월쉬 행렬
import sys
input = sys.stdin.readline

def divide(n, r, s, e):
    
    if n == 0:
        return 1

    mid = size[n] // 2

    if s < mid and e >= mid:
        h1 = divide(n-1, r % mid, s, mid-1)
        h2 = divide(n-1, r % mid, 0, e-mid)

        if r >= mid:
            return h1 - h2
        else:
            return h1 + h2
    else:
        if r >= mid and e >= mid:
            return -divide(n-1, r % mid, s % mid, e % mid)
        else:
            return divide(n-1, r % mid, s % mid, e % mid)

size = [1] * 61
for i in range(1, 61):
    size[i] = size[i-1] * 2
    
while True:
    N, R, S, E = map(int,input().split())

    if N == -1:
        break

    if R == 0:
        print(E - S + 1)
        continue

    print(divide(N, R, S, E)) 
