# 신입 사원
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())

    scores = []
    cnt = N
    
    for j in range(N):
        s1, s2 = map(int,input().split())
        scores.append((s1, s2))

    scores.sort()
    
    min_s1 = scores[0][0]
    min_s2 = 100001
    
    for i in range(N):
        s1, s2 = scores[i]

        if s1 != min_s1 and min_s2 < s2:
            cnt -= 1

        min_s2 = min(min_s2, s2)

    print(cnt)
            