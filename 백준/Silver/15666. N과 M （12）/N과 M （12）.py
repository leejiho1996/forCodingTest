# N과 M (12)
import sys
input = sys.stdin.readline

def backtrack(limit, length, word):
    if len(word) == m:
        print(*word)
        return

    for i in range(limit, length):
        word.append(seq[i])
        backtrack(i, length, word)
        word.pop()

n, m = map(int,input().split())
seq = set(map(int,input().split()))
seq = list(seq)
seq.sort()

backtrack(0, len(seq), [])
