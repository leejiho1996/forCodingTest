# 폴리오미노
import sys
input = sys.stdin.readline

board = input().rstrip()
parts = board.split(".")

for i in range(len(parts)):

    cur = parts[i]
    le = len(cur)
    
    if cur == '':
        continue

    if le % 2 == 1:
        print(-1)
        exit()

    tmp = ""

    tmp += le // 4 * "AAAA"

    if le % 4:
        tmp += "BB"

    parts[i] = tmp

print(".".join(parts))
