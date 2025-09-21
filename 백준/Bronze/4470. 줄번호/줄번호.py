import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    s = input().rstrip()
    print(str(i+1)+'.', s)