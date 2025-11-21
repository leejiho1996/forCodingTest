# 진우의 비밀번호
import sys
input = sys.stdin.readline

N = int(input())
password = input().rstrip()
order = "abcdefghijklmnopqrstuvwxyz"

result = 0

for i in range(len(password)):
    cur = password[i]
    idx = order.find(cur)

    for j in range(N-i):
        result += idx * (26**(j))

    result += 1
    
print(result)
