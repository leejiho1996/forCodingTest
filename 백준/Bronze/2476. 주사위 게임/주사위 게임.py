import sys
input = sys.stdin.readline

n = int(input())

total = 0
for i in range(n):
    a, b, c = map(int,input().split())
    
    if a == b == c:
        cur = 10000 + (a * 1000)
    elif a == b or b == c or a == c:
        if a == b:
            cur = 1000 + (a * 100)
        elif b == c:
            cur = 1000 + (b * 100)
        else:
            cur = 1000 + (c * 100)
    else:
        cur = max(a, b, c) * 100
        
    total = max(total, cur)

print(total)