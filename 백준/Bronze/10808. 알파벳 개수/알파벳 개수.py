# 알파벳 갯수
import sys
input = sys.stdin.readline

w = input().rstrip()
l = [0] * 26

for i in w:
    l[ord(i)-ord('a')] += 1

print(*l)