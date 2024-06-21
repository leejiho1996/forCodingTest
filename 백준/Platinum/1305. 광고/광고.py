import sys
input = sys.stdin.readline

def preKMP(word):
    length = len(word)
    f = [-1] * length
    idx = -1

    for i in range(1, length):
        while idx >= 0 and word[idx+1] != word[i]:
            idx = f[idx]

        if word[idx+1] == word[i]:
            f[i] = idx + 1
            idx += 1

    return f 
    

l = int(input())

word = input().rstrip()

word_kmp = preKMP(word)

print(l - (word_kmp[-1] + 1))
