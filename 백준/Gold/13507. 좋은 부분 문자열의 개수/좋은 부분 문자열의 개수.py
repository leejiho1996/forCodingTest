# 좋은 부분 문자열의 개수
import sys
input = sys.stdin.readline
from collections import deque

word = input().strip()
bad = input().strip()
limit = int(input())

bad_check = [int(c) for c in bad]
sett = set()

for i in range(len(word)):
    bad_count = 0
    h = ""
    for j in range(i, len(word)):
        if bad_check[ord(word[j]) - 97] == 0:
            bad_count += 1
        if bad_count > limit:
            break
        h += word[j]
        sett.add(h)

print(len(sett))

