# 가르침
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

if k < 5:
    print(0)
    exit()

base = ["a", "n", "t", "c", "i"]
word_list = []
is_used = [False] * 26

for i in base:
    is_used[ord(i) - 97] = True

maxx = 0
def dfs(start, length):

    global maxx
    
    if length == k - 5:
      
        cnt = 0 
        for i in range(n):
            word = word_list[i]
            possible = True

            for j in word:
                if not is_used[ord(j) - 97]:
                    possible = False
                    break

            if possible:
                cnt += 1
                
        maxx = max(maxx, cnt)
        return
    
    for i in range(start, 32 - k + length): # k 는 5 이상
        
        if not is_used[i]:
            is_used[i] = True
            dfs(i, length+1)
            is_used[i] = False
        
for i in range(n):
    word = input().rstrip()
    word = word.replace("anta", "")
    word = word.replace("tica", "")
    word_list.append(word)

dfs(0, 0)

print(maxx)
