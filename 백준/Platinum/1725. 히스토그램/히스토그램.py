# 히스토그램 (1725)
import sys
input = sys.stdin.readline

n = int(input())

hist = [0] + [int(input()) for _ in range(n)] + [0]

maxx = 0
stack = [0]

for i in range(1, n+2):    
    while stack and hist[stack[-1]] > hist[i]:
        num = stack.pop()
        maxx = max(maxx, (i-1-stack[-1]) * hist[num])

    stack.append(i)

print(maxx)
