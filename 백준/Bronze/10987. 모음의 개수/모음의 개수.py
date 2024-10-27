import sys
input = sys.stdin.readline
n = input().rstrip()
s = {"a", "e", "i", "o", "u"}
cnt = 0
for i in n:
    if i in s:
        cnt += 1
print(cnt)