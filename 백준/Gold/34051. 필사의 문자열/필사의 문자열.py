import sys
input = sys.stdin.readline

N = int(input())
W = input().rstrip()

minn = [5001] * N
candi = []

for i in range(N):
    for j in range(i+1, N):
        if W[i] < W[j] and minn[j] == 5001:
            minn[j] = i
            candi.append((i, j))

result = W

for i, j in candi:
    tmp = W[:i] + W[i:j+1][::-1] + W[j+1:]

    if tmp > result:
        result = tmp

print(result)

