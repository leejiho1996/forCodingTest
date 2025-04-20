# 점숫자
import sys
input = sys.stdin.readline

T = int(input())
dic1 = {}
dic2 = {}
cur = (1, 1)
cnt = 1
limit = 1

for i in range(1, 50001):
    dic1[cnt] = cur
    dic2[cur] = cnt

    if cur[1] == 1:
        limit += 1
        cur = (1, limit)
    else:
        cur = (cur[0]+1, cur[1]-1)

    cnt += 1
    
for i in range(T):
    a, b = map(int,input().split())
    p1 = dic1[a]
    p2 = dic1[b]

    p = (p1[0]+p2[0], p1[1]+p2[1])
    print(dic2[p])
    
