# 벼룩 시장
import sys
input = sys.stdin.readline
import heapq as hq

N = int(input())
nums = list(map(int,input().split()))
plus = []
minus = []
result = 0

for i in range(N):
    if nums[i] < 0:
        hq.heappush(minus, (i, nums[i]))
    elif nums[i] > 0:
        hq.heappush(plus, (i, nums[i]))

while minus:
    idx, minus_num = hq.heappop(minus)

    while minus_num and plus:
        p_idx, plus_num = hq.heappop(plus)

        if minus_num + plus_num > 0:
            result += -minus_num * abs(idx - p_idx)
            plus_num += minus_num
            minus_num = 0
            hq.heappush(plus, (p_idx, plus_num))
        else:
            result += plus_num * abs(idx - p_idx)
            minus_num += plus_num

print(result)
