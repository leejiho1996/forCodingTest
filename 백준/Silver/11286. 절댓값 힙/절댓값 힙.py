# 절대값 힙
import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    command = int(input())

    if command == 0:
        if len(arr) == 0:
            print(0)
        else:
            num = heapq.heappop(arr)
            if num[1] == -1:
                print(-num[0])
            else:
                print(num[0])
    else:
        if command > 0:
            heapq.heappush(arr, (command, 1))
        elif command < 0:
            heapq.heappush(arr, (-command, -1))
