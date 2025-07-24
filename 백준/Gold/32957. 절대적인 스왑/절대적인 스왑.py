# 절대적인 스왑
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

maxx = 0
minn = 1000001
value= 0

for i in range(1, N + 1):
    num = nums[i-1]
    maxx = max(maxx, min(num, i)) # 각 위치의 작은 값 중 최대값
    minn = min(minn, max(num, i)) # 각 위치의 큰 값 중 최소값
    value += abs(num - i) # 원래의 가치

print(value + 2 * max(0, maxx - minn))
