# 가르침
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

if k < 5:
    print(0)
    exit()

base = {"a", "n", "t", "c", "i"}

alphabet = {}

for i in range(26):
    alphabet[chr(97+i)] = 0

word_set = []
candi = []

def dfs(w, depth):
    
    next_chr = chr(96+depth)
    
    if len(w) == k - 5:
        candi.append(w)
        return
    
    if (26 - depth+1) + len(w) < k - 5: # (26-depth) -> 남은 알파벳 
        return

    dfs(w, depth+1)

    if next_chr not in base:    
        dfs(w+next_chr, depth+1)
    

for i in range(n):
    word = set(input().rstrip())
    word_set.append(word-base)

dfs("", 1)

maxx = 0
for i in range(len(candi)):
    check = set(candi[i])
    cnt = 0
    for j in range(n):
        if len(word_set[j].difference(check)) == 0:
            cnt += 1        
    maxx = max(maxx, cnt)

print(maxx)
