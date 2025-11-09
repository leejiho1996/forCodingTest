# 요세푸스 문제
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
li = [i for i in range(1, N+1)]
result = []

ptr = 0

if N == 1:
    print("<1>")
    exit()
    
while li:
    ptr += (K-1)
    ptr %= len(li)
    
    rm_idx = li.index(li[ptr])
    result.append(li[ptr])
    
    li.remove(li[ptr])

    if len(li) == 0:
        break
    
    ptr = (rm_idx) % len(li)

for i in range(N):
    if i == 0:
        print("<", result[i], ",", sep="", end = " ")
    elif i == N-1:
        print(result[i], ">", sep="")
    else:
        print(result[i], ",", sep="", end = " ")

