# 토너먼트
import sys
input = sys.stdin.readline

n, kim, lim = map(int,input().split())

divide = 2
cnt = 1

while True:
    if (lim - 1) // divide == (kim -1) // divide:
        print(cnt)
        break
    else:
        divide *= 2
        cnt += 1
