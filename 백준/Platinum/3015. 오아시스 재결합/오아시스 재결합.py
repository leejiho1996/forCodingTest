# 오아시스 재결합
import sys
input = sys.stdin.readline

n = int(input())
limit = float('inf')
num = []

num = [int(input()) for _ in range(n)]

num.append(limit)

stack = [(num[0], 0, 0)]
cnt = 0

for i in range(1, n+1):
    total = 0
    cur = num[i]
    sa = 0
    maxx = 0
    
    while stack and stack[-1][0] <= num[i]:
        number, r, same = stack.pop()

        if maxx <= number:
            total += 1
            
        if number == num[i]:
            sa = (same + 1)

        total += same

        cnt += r
        
        maxx = max(number, maxx)

    if stack:
        total += 1
            
    stack.append((num[i], total, sa))

print(cnt)