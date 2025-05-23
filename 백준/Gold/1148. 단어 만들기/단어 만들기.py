# 단어 만들기
import sys
input = sys.stdin.readline

graph = [[0] * 26 for _ in range(200000)]
idx = 0
PAD = ord("A")

while True:
    cur = input().rstrip()

    if cur == "-":
        break

    for c in cur:
        graph[idx][ord(c)-PAD] += 1

    idx += 1

while True:
    cur = input().rstrip()

    if cur == "#":
        break

    charCnt = [0] * 26
    for c in cur:
        charCnt[ord(c)-PAD] += 1

    minChar = ""
    maxChar = ""
    minn = 200001
    maxx = 0

    midCnt = [0] * 26

    for i in range(idx):
        check = True

        for j in range(26):
            if graph[i][j] > charCnt[j]:
                check = False
                break

        if not check:
            continue

        for j in range(26):
            if graph[i][j] > 0:
                midCnt[j] += 1

    for i in range(26):
        if charCnt[i] > 0:
            minn = min(minn, midCnt[i])
            maxx = max(maxx, midCnt[i])

    for i in range(26):
        if charCnt[i] == 0:
            continue

        if midCnt[i] == minn:
            minChar += chr(PAD+i)

        if midCnt[i] == maxx:
            maxChar += chr(PAD+i)

    print(minChar, minn, maxChar, maxx)
