# 등수구하기
import sys
input = sys.stdin.readline

n, t, p = map(int,input().split())
if n == 0:
    print(1)
    exit()

score = list(map(int,input().split()))
sett = set(score)
reverse = score[::-1]

idx = n
min_idx = n

if t in score:
    idx = score.index(t)

for i in range(n):
    if score[i] >= t:
        continue
    else:
        min_idx = i
        break

if min_idx > p - 1:
    print(-1)
else:
    print(min(min_idx+1, idx+1))
