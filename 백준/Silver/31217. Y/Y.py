# Y
import sys
input = sys.stdin.readline

# n을 루트로하는 Y를 계산 ((n과 연결된 노드 크기) C 3)
def cal(n):
    size = link[n]
    return size * (size-1) * (size-2) // 6 % MOD

N, M = map(int,input().split())
link = [0] * (N+1)
MOD = 1_000_000_007

# 연결정보를 입력받고 저장
for i in range(M):
    a, b = map(int,input().split())
    link[a] += 1
    link[b] += 1

result = 0
for i in range(1, N+1):
    result += cal(i)
    result %= MOD

print(result)
    
