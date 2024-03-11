# 회의실 배정
import sys
input = sys.stdin.readline

time = []
n = int(input())

for i in range(n):
    s, e = map(int,input().split())
    time.append((s,e))

time.sort(key=lambda x:(x[1], x[0]))

end_time = 0
cnt = 0

for start, end in time:
    if start < end_time:
        continue
    else:
        end_time = end
        cnt += 1

print(cnt)