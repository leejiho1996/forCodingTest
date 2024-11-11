# 문자열 게임2
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    word = input().rstrip()
    k = int(input())

    char_idx = {}
    minn = len(word)
    maxx = 0
    
    for j in range(len(word)):
        char = word[j]

        if char not in char_idx:
            char_idx[char] = [j]
        else:
            char_idx[char].append(j)

        if len(char_idx[char]) >= k:
            minn = min(minn, char_idx[char][-1] - char_idx[char][-1-k+1]+1)
            maxx = max(maxx, char_idx[char][-1] - char_idx[char][-1-k+1]+1)

    if maxx == 0:
        print(-1)
        continue

    print(minn, maxx)
            
   