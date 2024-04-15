# 최대 힙
import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []

for i in range(n):
    command = int(input())

    if command == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -command)