# 물류 작업 최적화
import sys
input = sys.stdin.readline

N = int(input())
items = list(map(int,input().split()))

aggSum = [0] * N
aggSum[0] = items[0]

plus = [0] * N
minus = [-1] * N

last = -1
for i in range(1, N):
    aggSum[i] = items[i] + aggSum[i-1]    
    minus[i] = last

    if aggSum[i] < 0:    
        last = i

maxx = -float('inf')
maxIdx = -1
for i in range(N-1, -1, -1):
    if aggSum[i] > maxx:
        maxx = aggSum[i]
        maxIdx = i
        plus[i] = maxIdx
    else:
        plus[i] = maxIdx

for i in range(N):
    if minus[i] == -1:
        print(aggSum[plus[i]], end = " ")
    else:
        print(aggSum[plus[i]] - aggSum[minus[i]], end = " ")
