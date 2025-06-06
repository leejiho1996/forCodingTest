# 카드 게임
import sys
input = sys.stdin.readline

def solve(left, right, turn):

    if left > right:
        return 0

    if dp[left][right] != -1:
        return dp[left][right]
    else:
        dp[left][right] = 0

    if turn == 1:
       dp[left][right] =  min(solve(left+1, right, 1-turn),
                              solve(left, right-1, 1-turn))
    else:   
        dp[left][right] = max(solve(left+1, right, 1-turn) + cards[left],
                          solve(left, right-1, 1-turn) + cards[right])

    return dp[left][right]

T = int(input())

for i in range(T):
    N = int(input())
    cards = list(map(int,input().split()))
    dp = [[-1] * N for _ in range(N)]

    print(solve(0, N-1, 0))
    
