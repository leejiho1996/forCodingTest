# 주식
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    costs = list(map(int,input().split()))
    stack = []
    result = 0

    while costs:
        cur = costs.pop()

        if costs and cur < costs[-1]:
            continue

        while costs and costs[-1] <= cur:
            result += cur - costs.pop()

    print(result)
