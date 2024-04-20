# 공넣기
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

ball = [0]*n

for i in range(m):
    start, end, ball_num = map(int,input().split())

    for j in range(start-1, end):
        ball[j] = ball_num

print(*ball)