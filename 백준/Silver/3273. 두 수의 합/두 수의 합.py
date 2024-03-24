# 두 수의 합
import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))
num.sort()

x = int(input())

start = 0
end = n-1

cnt = 0
while start < end:
    if num[start] + num[end] >= x:
        if num[start] + num[end] == x:
            cnt += 1
        end -= 1
    else:
        start += 1

print(cnt)
