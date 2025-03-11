# 선 긋기
import sys
input = sys.stdin.readline

N = int(input())
lines = []
result = 0

for i in range(N):
    x, y = map(int,input().split())
    lines.append((x, y))

lines.sort()

start = lines[0][0]
end = lines[0][1]

for i in range(1, N):
    x, y = lines[i]

    if x <= end:
        if y > end:
            end = y
    else:
        result += (end - start)
        start = x
        end = y

result += (end - start)

print(result)
        
