# N과 M(3)

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
num_list = [i for i in range(1, n+1)]

def backtrack(m, word):
    if len(word) == m:
        print(' '.join(word))
        return

    for i in num_list:
        word += str(i)
        backtrack(m, word)
        word = word[:-1]

backtrack(m, '')

