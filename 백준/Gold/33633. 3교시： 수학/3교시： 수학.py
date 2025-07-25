# 3교시: 수학
import sys
input = sys.stdin.readline

def backtrack(cur, cnt):
    if cnt == N:
        result.add(cur)
        return

    if (cur - 1) % 3 == 0 and ((cur-1) // 3) % 2 == 1 and (cur-1) // 3 > 1:
        backtrack((cur - 1) // 3, cnt+1)

    backtrack(cur * 2, cnt + 1)

N = int(input())
result = set()

backtrack(1, 1)

print(len(result))

result = list(result)
result.sort()

for i in result:
    print(i)
