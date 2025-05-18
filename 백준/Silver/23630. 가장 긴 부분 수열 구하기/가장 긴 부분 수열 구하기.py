import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
cnt=[0]*20

for i in range(n):
    for j in range(20):
        if a[i] & (1 << j):
            cnt[j]+=1
result =0
for i in range(20):
    if result < cnt[i]:
        result = cnt[i]
print(result)