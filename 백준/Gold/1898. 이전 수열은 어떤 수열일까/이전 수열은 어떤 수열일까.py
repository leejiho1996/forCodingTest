# 이전 수열은 어떤 수열일까
import sys
input = sys.stdin.readline

N = int(input())
origin = []
idx = [-1] * (N+1)
result = [0] * N

# 숫자를 입력받고 인덱스를 저장
for i in range(N):
    num = int(input())
    origin.append(num)
    idx[num] = i

for i in range(N):
    cur = origin[i]
    # 이미 다른 숫자와 바꾼 숫자라면 패스
    if idx[cur] == -1:
        continue
    
    m1 = idx[cur-1] # 현재 숫자보다 1작은 숫자의 인덱스

    if m1 < idx[cur]:
        result[i] = cur
    else:
        result[i] = cur-1
        result[m1] = cur

        idx[cur-1] = -1
        idx[cur] = -1

for i in result:
    print(i)
    