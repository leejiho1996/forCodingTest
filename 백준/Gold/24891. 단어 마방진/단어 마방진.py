# 단어 마방진
import sys
input = sys.stdin.readline

def check(arr):

    for i in range(L):
        row = arr[i]
        col = ""
        for j in range(L):
            col += arr[j][i]

        if row != col:
            return False

    return True

def solve(cur, cnt):

    if cnt == L:
        if check(cur):
            for i in cur:
                print(i)
            exit()
        return

    for i in range(N):
        if visited[i]:
            continue

        if cur and cur[0][cnt] != words[i][0]:
            continue

        visited[i] = 1
        cur.append(words[i])

        solve(cur, cnt+1)

        cur.pop()
        visited[i] = 0
        
L, N = map(int,input().split())
words = []
visited = [0] * N

for i in range(N):
    words.append(input().rstrip())

words.sort()

solve([], 0)
print("NONE")
