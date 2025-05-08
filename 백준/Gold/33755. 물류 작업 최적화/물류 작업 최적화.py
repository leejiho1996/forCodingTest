import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

L = [0]*N
L[0] = A[0]
for i in range(1, N):
    L[i] = max(A[i], L[i-1] + A[i])
    
R = [0]*N
R[N-1] = A[N-1]
for i in range(N-2, -1, -1):
    R[i] = max(A[i], R[i+1] + A[i])

ans = [L[i] + R[i] - A[i] for i in range(N)]
print(" ".join(map(str, ans)))
