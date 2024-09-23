import sys
input = sys.stdin.readline

l = int(input())
s= list(map(int,input().split()))
s.sort()
n = int(input())

min_num = 1
max_num = -1

for i in range(l):
    if s[i] <= n :
        min_num = s[i] + 1 

    if s[i] > n and max_num == -1:
        max_num = s[i] - 1

if min_num == n + 1 or max_num == -1:
    print(0)
else:
    result = 0
    possible = max_num - n + 1

    for i in range(min_num, n):
        result += possible
    result += max_num - n
    
    print(result)
