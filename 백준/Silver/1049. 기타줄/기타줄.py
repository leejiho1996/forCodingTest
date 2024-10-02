# 기타줄
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

min_p = 1001
min_s = 1001
result = 0

for i in range(m):
    p, s = map(int,input().split())
    min_p = min(min_p, p)
    min_s = min(min_s, s)

package_pos = n // 6

if min_p / 6 < min_s:
    result += package_pos * min_p
    n -= package_pos * 6
    result += min(min_p, min_s * n)
else:
    result += min_s * n
        
print(result)
