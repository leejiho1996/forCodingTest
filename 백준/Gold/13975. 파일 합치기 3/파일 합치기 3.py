# 파일 합치기 3
import sys
input = sys.stdin.readline
import heapq as hq

T = int(input())

for i in range(T):
    K = int(input())
    files = list(map(int,input().split()))
    hq.heapify(files)
    result = 0
    
    while len(files) > 1:
        n1 = hq.heappop(files)
        n2 = hq.heappop(files)
        result += n1 + n2
        
        hq.heappush(files, n1+n2)
        
    print(result)
