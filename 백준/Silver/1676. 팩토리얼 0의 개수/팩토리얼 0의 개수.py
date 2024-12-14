# 팩토리얼 0의 개수
import sys
input = sys.stdin.readline

n = int(input())
start = 1
for i in range(n):
    start *= i+1

toList = list(str(start))
cnt = 0
while toList[-1] == "0":
    toList.pop()
    cnt += 1
print(cnt)
