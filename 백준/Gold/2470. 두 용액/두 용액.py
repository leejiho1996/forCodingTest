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
    if abs(num[end]+num[start]) < prev:
        prev = abs(num[start]+num[end])
        if prev < min_prev:
            min_prev = prev
            p_start = num[start]
            p_end = num[end]
        end -= 1
        
    else:
        start += 1
        prev = 2_000_000_001
        end = min(n-1, end+1)
                  
print(p_start, p_end)