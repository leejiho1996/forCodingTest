# Important Message
import sys
input = sys.stdin.readline

sett = set()
result = 0

N = int(input())

for i in range(N):
    cur = input().rstrip()
    sett.add(cur)

M = int(input())

for i in range(M):
    cur = input().rstrip()

    if cur in sett:
        result += 1

print(result)
