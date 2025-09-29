# 올라올라
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
bigger = []
result = [0] * N

for i in range(N):
    if i == 0:
        bigger.append(i)
        continue
    
    if nums[i] < nums[bigger[-1]]:
        continue
    else:
        bigger.append(i)

cnt = 0
for i in range(N):
    cur = bigger[cnt]

    if cur >= i:
        result[i] = cur
    else:
        result[i] = -1
    
    if i == cur and cnt < len(bigger)-1:
        cnt += 1

ret = 0
for i in range(N):
    if N - i <= ret:
        break

    if result[i] < 0:
        ret = N - i
        break
    
    ret = max(ret, result[i] - i)

print(ret+1)
