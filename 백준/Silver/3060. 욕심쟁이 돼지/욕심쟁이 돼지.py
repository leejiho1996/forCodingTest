# 욕심쟁이 돼지
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    eat = sum(list(map(int,input().split())))

    total = 0
    cnt = 1

    while eat <= N:
        eat *= 4
        cnt += 1
        
    print(cnt)
        
