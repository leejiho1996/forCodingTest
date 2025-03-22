# 풍선 맞추기
import sys
input = sys.stdin.readline

N = int(input())
balloons = list(map(int,input().split()))
exists = [0] * 1000002
cnt = 0

for i in balloons:
    if exists[i+1]:
        exists[i+1] -= 1
    else:
        cnt += 1
        
    exists[i] += 1

print(cnt)