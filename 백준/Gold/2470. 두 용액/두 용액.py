# 두 용액

import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))
num.sort()

start = 0
end = n-1

prev = 2_000_000_001
min_prev = 2_000_000_001


while start < end:
    s = num[start] + num[end]
    if abs(s) < prev:
        prev = abs(s)
        p_start = num[start]
        p_end = num[end]

    if s < 0:
        start += 1
    elif s > 0:
        end -= 1
    else:
        break
    
print(p_start, p_end)

# 양수 음수 체크 
