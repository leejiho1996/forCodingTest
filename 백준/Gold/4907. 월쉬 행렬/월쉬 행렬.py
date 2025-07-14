# 월쉬 행렬
import sys
input = sys.stdin.readline

def divide(n, r, s, e):
    
    if n == 0:
        return 1

    mid = size[n] // 2

    # 범위가 두 부분으로 나눠지는 경우
    if s < mid and e >= mid:
        h1 = divide(n-1, r % mid, s, mid-1)
        h2 = divide(n-1, r % mid, 0, e-mid)

        if r >= mid:
            return h1 - h2
        else:
            return h1 + h2
    else: # 한 부분에 있는 경우
        if r >= mid and e >= mid: # 만약 4 사분면이면 음수값 리턴
            return -divide(n-1, r % mid, s % mid, e % mid)
        else:
            return divide(n-1, r % mid, s % mid, e % mid)

size = [1] * 61
for i in range(1, 61):
    size[i] = size[i-1] * 2

result = []
while True:
    N, R, S, E = map(int,input().split())

    if N == -1:
        break

    if R == 0:
        result.append(E - S + 1)
        continue

    result.append(divide(N, R, S, E)) 

print(*result)
