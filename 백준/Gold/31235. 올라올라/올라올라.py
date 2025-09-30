# 올라올라
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
bigger = []

for i in range(N):
    if i == 0:
        bigger.append(i)
        continue
    
    if nums[i] < nums[bigger[-1]]:
        continue
    else:
        bigger.append(i)

cnt = 0
ret = 0
for i in range(N):
    cur = bigger[cnt]

    if cur >= i:
        ret = max(cur - i, ret)
    else:
        ret = max(ret, N - i)
        break
        
    if i == cur and cnt < len(bigger)-1:
        cnt += 1

print(ret+1)
