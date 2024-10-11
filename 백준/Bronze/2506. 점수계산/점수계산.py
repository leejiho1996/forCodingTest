import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))

add = 1
result = 0
for i in range(n):
    if num_list[i] == 1:
        result += add
        add += 1
    else:
        add = 1

print(result)
