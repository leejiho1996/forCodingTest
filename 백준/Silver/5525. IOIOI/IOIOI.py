# IOIOI
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
Pn = "IO" * n + "I"
string = input().rstrip()
cnt = 0

while True:
    start_idx = string.find(Pn)

    if start_idx == -1:
        break
    else:
        cnt += 1
        string = string[start_idx + 2:]

print(cnt)
