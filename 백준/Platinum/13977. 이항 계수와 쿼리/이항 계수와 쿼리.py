# 이항 계수와 쿼리
import sys
input = sys.stdin.readline

# 4,000,000까지의 팩토리얼 저장
def init():
    for i in range(1, 4_000_001):
        dp[i] = (dp[i-1] * i) % MOD 

# 분할 정복으로 MOD-2제곱 계산
def cal(num, power):

    if power == 1:
        return num

    res = cal(num, power//2)

    if power % 2 == 1:
        return res * res * num % MOD
    else:
        return res* res % MOD

dp = [0] * (4_000_001)
dp[0] = 1
MOD = 1_000_000_007

init()

N = int(input())

for i in range(N):
    A, B = map(int,input().split())
    # 페르마의 소정리
    # 1. a^P = a (mod P)
    # 2. a^(p-1) = 1 (mod P)
    # 3. a^(P-2) = 1/a (mod P)
    # N!/K!(N-K)! -> N! * (K!(N-K!))^-1
    print(dp[A] * cal(dp[B]*dp[A-B], MOD-2) % MOD)

