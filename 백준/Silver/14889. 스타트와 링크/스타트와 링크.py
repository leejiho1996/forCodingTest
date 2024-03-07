# 스타트와 링크
import sys
input = sys.stdin.readline

n = int(input())

s = [list(map(int,input().split())) for _ in range(n)]

arr = [0] * (n//2)

minn = 10000

def score(arr, pick, cnt):
    summ = 0
    if len(pick) == 2:
        return s[pick[0]][pick[1]] + s[pick[1]][pick[0]]

    for i, j in enumerate(arr):
        if cnt > 1 and j <= pick[-1]:
            continue
        pick.append(j)
        summ += score(arr, pick, cnt+1)
        pick.pop()
    
    return summ    
        

def team(count):
    global minn
    
    if count == n//2:
        start = []
        link = []

        for i in range(n):
            if i in arr:
                start.append(i)
            else:
                link.append(i)
     
        start_score = score(start, [], 1)
        link_score = score(link, [], 1)

        minn = min(minn, abs(start_score-link_score))
        return

    for i in range(1, n):
        if arr[count-1] >= i:
            continue
        arr[count] = i
        team(count+1)
            
        
team(1)
print(minn)