# 주유소
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))

summ = sum(dist)
result = 0

seq = 0
while summ:
    summ -= dist[seq]
    result += cost[seq] * dist[seq]
    for i in range(seq+1 , n-1):
        if cost[seq] > cost[i]:
            seq = i
            break
        else:
            result += cost[seq] * dist[i]
            summ -= dist[i]             

print(result)
