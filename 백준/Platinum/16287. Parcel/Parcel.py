# Parcel (중간부터 나눠서)
import sys
input = sys.stdin.readline

def solution():
    W, N = map(int,input().split())
    A = list(map(int,input().split()))

    two_sum = [False] * W

    A.sort()

    for i in range(2, N-1):
        
        for j in range(i-1):

            if A[i-1] + A[j] >= W:
                break
            
            two_sum[A[i-1] + A[j]] = True

        for j in range(i+1, N):
            num = W - (A[i] + A[j])

            if num <= 0 or num >= W:
                break

            if two_sum[num]:
                print("YES")
                exit()

    print("NO")

solution()
