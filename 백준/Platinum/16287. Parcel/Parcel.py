# Parcel
import sys
input = sys.stdin.readline

W, N = map(int,input().split())
A = list(map(int,input().split()))

two_sum = [(-1,-1) for _ in range(W+1)]
num_set = [set()] * N

for i in range(N):
    for j in range(i+1, N):
        num = A[i] + A[j]

        if num >= W+1:
            continue

        if two_sum[num] == (-1, -1):
            two_sum[num] = (i, j)
            

for i in range(N):
    for j in range(i+1, N):
        find = W - (A[i] + A[j])

        if find <= 0 :
            continue
        
        if two_sum[find] == (-1, -1):
            continue

        x, y = two_sum[find]
        
        if i != x and i != y and j != x and j != y:
            print("YES")
            exit()

print("NO")



