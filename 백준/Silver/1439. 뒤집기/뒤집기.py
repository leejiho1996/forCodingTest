# 뒤집기
import sys
input = sys.stdin.readline

s = input().rstrip()

zero = 0
one = 0

start = s[0]
tmp = ""
for i in range(1, len(s)):

    if s[i] == start:
        pass
    else:
        if s[i] == "0":
            one += 1
            tmp = ""
            start = "0"
        else:
            zero += 1
            tmp = ""
            start = "1"

if s[i] == "0":
    zero += 1
else:
    one += 1

print(min(zero, one))
