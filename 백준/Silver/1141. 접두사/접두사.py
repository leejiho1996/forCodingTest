# 접두사
import sys
input = sys.stdin.readline

n = int(input())

suff = []

for i in range(n):
    w = input().rstrip()
    suff.append(w)

cnt = 0
suff = list(set(suff))

for i in range(len(suff)):
    word = suff[i]
    lenn = len(word)
    check = True
    for j in range(len(suff)):
        if j == i :
            continue
        oppo = suff[j]

        if len(oppo) >= lenn and oppo[:lenn] == word:
            check = False
            break
    if check:
        cnt += 1

print(cnt)
