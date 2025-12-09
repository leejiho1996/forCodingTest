import sys
input = sys.stdin.readline

N = int(input())
W = input().rstrip()
sortedW = sorted(W, reverse=True)

s = -1
maxx = 'a'

for i in range(N):
    if s == -1 and W[i] != sortedW[i]:
        s = i

    if s !=-1 and W[i] > maxx:
        maxx = W[i]

if s == -1:
    print(W)
    exit()

result = W
for i in range(s+1, N):

    if W[i] != maxx:
        continue

    tmp = W[:s] + W[s:i+1][::-1] + W[i+1:]

    if tmp > result:
        result = tmp

print(result)
