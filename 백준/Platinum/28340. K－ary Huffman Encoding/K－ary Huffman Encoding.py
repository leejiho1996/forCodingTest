# K-ary Huffman Encoding
import sys
input = sys.stdin.readline
import heapq as hq

T = int(input())

for _ in range(T):
    N, K = map(int,input().split())
    times = list(map(int,input().split()))
    hq.heapify(times)
    result = 0
    
    needs = ((K - 1) - ((N - 1) % (K - 1))) % (K - 1)
    
    for i in range(needs):
        hq.heappush(times, 0)
    
    while len(times) > 1:
        tmp = 0

        for k in range(K):
            cur = hq.heappop(times)
            tmp += cur
            result += cur

        hq.heappush(times, tmp)
    
    print(result)
