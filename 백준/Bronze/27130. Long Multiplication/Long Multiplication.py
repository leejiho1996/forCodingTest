# Long Multiplication
import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

print(A)
print(B)

for i in range(len(B)-1, -1, -1):
    print(int(B[i]) * int(A))

print(int(A) * int(B))
