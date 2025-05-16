# 중앙값 구하기
import sys
input = sys.stdin.readline
import heapq as hq

T = int(input())

for i in range(T):
    M = int(input())
    rep = M // 10
    cnt = 0
    mid = 0
    result = []
    
    max_que = []
    min_que = []

    while (rep >= 0):
        nums = list(map(int,input().split()))

        for cur in nums:
            
            if cnt == 0:
                mid = cur
                cnt += 1
                result.append(mid)
                continue

            if cur > mid:
                hq.heappush(max_que, cur)
            else:
                hq.heappush(min_que, -cur)

            if cnt % 2 == 0:
                if len(max_que) > len(min_que):
                    hq.heappush(min_que, -mid)
                    mid = hq.heappop(max_que)
                elif len(min_que) > len(max_que):
                    hq.heappush(max_que, mid)
                    mid = -hq.heappop(min_que)
                
                result.append(mid)

            cnt += 1

        rep -= 1

    print(len(result))

    for i in range(len(result)):
        print(result[i], end = " ")

        if (i+1) % 10 == 0 and i != len(result) - 1:
            print()
    print()
        
