# 점프 숨바꼭질
import sys
input = sys.stdin.readline
import math

K = int(input())

if K == 0:
    print(0)
    exit()
    
jump = 2**int(math.log(abs(K), 2))
cnt = 0

while jump:
    if K < 0:
        K += jump
    else:
        K -= jump

    jump //= 2
    cnt += 1
    
if K == 0:
    print(cnt)
else:
    print(-1)

