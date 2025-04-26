# Draw A Perfect Circle
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dists = []
result = 0

for i in range(N):
    x, y = map(int,input().split())
    dist = (x**2 + y**2)**0.5
    dists.append(dist)

dists.sort()
end = 0

for i in range(N):
    minn = dists[i]
    maxx = minn + K

    while end < N and dists[end] <= maxx:
        end += 1

    result = max(result, 100/N * (end - i))

print(f'{result:.6f}')
