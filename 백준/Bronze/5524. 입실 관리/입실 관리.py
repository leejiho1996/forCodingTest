import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    w = input().rstrip()
    print(w.lower())