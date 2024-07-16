import sys
input = sys.stdin.readline
a, b = map(int, input().split())
a = list(map(int, list(str(a))))
b = list(map(int, list(str(b))))
cnt = 0
for i in a:
    for j in b:
        cnt += i * j
print(cnt)
