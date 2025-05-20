# 이진수 나눗셈
import sys
input = sys.stdin.readline

N = int(input())
M = input().rstrip()
K = int(input())

for i in range(K):
    if i == N:
        break
    
    if M[N-i-1] == "1":
        print("NO")
        exit()

print("YES")
