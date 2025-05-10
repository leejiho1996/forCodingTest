# Y
import sys
input = sys.stdin.readline

def cal(n):
    size = len(graph[n])
    return size * (size-1) * (size-2) // 6 % MOD

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
MOD = 1_000_000_007

for i in range(M):
    a, b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(1, N+1):
    result += cal(i)
    result %= MOD

print(result)
    
