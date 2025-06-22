# 제곱 ㄴㄴ 수
import sys
input = sys.stdin.readline

minn, maxx = map(int,input().split())
result = 0
cnt = maxx - minn + 1
visited = [0] * cnt

cur = 2
while cur**2 <= maxx:

    sqr = cur**2

    if minn % sqr == 0:
        start = 0
    else:
        start = sqr * (minn // sqr + 1) - minn

    for i in range(start, cnt, sqr):
        visited[i] = 1

    cur += 1

for i in range(cnt):
    if visited[i] == 0:
        result += 1
    
print(result)
