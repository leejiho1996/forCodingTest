# 작업
import sys
input = sys.stdin.readline

N = int(input())
time = [0] * N
res = [0] * N
front = [0] * N
tail = [[] for _ in range(N)]

stack = []

mx = 0

for i in range(N):
    tmp = list(map(int,input().split()))

    time[i] = tmp[0]
    front[i] = tmp[1]

    for j in range(tmp[1]): # 선행작업들의 리스트에 추가
        tail[tmp[2+j]-1].append(i)

    if tmp[1] == 0: # 선행작업이 없다면 스택에 추가
        stack.append((i, tmp[0]))
        res[i] = tmp[0]

while stack:

    cur, ct = stack.pop() # 끝난 작업과 끝난 시간
    mx = max(mx, ct)

    for j in (tail[cur]):
        front[j] -= 1

        res[j] = max(res[j], time[j] + ct)
        
        if front[j] == 0:
            stack.append((j, res[j]))

print(mx)
