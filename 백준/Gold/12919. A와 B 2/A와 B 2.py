# A와 B 2
import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def dfs(word, target):
    if word == target:
        return 1

    if len(word) >= len(target):
        return 0

    if target[-1] == "A":
        if (dfs(word, target[:-1])):
            return 1

    if target[0] == "B":
        if (dfs(word, target[::-1][:-1])):
            return 1

    return 0

print(dfs(s, t))
