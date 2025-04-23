# 벼룩 시장
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
plus = []
minus = []
result = 0

for i in range(N):
    if nums[i] < 0:
        minus.append((i, nums[i]))
    elif nums[i] > 0:
        plus.append((i, nums[i]))

m = 0
p = 0

while m < len(minus):
    midx, minus_num = minus[m]

    while minus_num:
        pidx, plus_num = plus[p]
        
        if minus_num + plus_num > 0:
            result += -minus_num * abs(midx - pidx)
            plus[p] = (pidx, plus_num + minus_num)
            minus_num = 0
        else:
            result += plus_num * abs(midx - pidx)
            minus_num += plus_num
            p += 1

    m += 1

print(result)
