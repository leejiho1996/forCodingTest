# 생존과 탈출
import sys
input = sys.stdin.readline

D, G = map(int,input().split())
boxes = []

for i in range(G):
    boxes.append(tuple(map(int,input().split())))

boxes.sort()

# dp[i] -> 높이 i에서 최대 생존 시간
dp = [-1] * (D+1)
dp[0] = 10

for i in range(G):
    T, F, H = boxes[i]

    for hei in range(D-1, -1, -1):
        if dp[hei] == -1 or dp[hei] < T:
            continue

        cur = dp[hei]

        if hei + H >= D:
            print(T)
            exit()

        dp[hei+H] = max(dp[hei+H], dp[hei])

        dp[hei] += F

print(max(dp))
        
